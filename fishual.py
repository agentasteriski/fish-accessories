import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x300")
        self.title("FISHUAL INTERFACE")
        self.create_widgets()

        style = ttk.Style()

        style.theme_use("clam")
        
    def create_widgets(self):

        #Set up tabs
        tabControl = ttk.Notebook(self)
  
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        tab4 = ttk.Frame(tabControl)
  
        tabControl.add(tab1, text ='About')
        tabControl.add(tab2, text ='Preprocess')
        tabControl.add(tab3, text ='Train')
        tabControl.add(tab4, text ='Inference')
        tabControl.pack(expand = 1, fill ="both")

        #ABOUT TAB
        tab1.label = ttk.Label(tab1, text ="FISHUAL INTERFACE")
        tab1.label.pack()
        tab1.label = ttk.Label(tab1, text ="A GUI for Fish Diffusion")
        tab1.label.pack()
        tab1.label = ttk.Label(tab1, text ="by AgentAsteriski, 2023")
        tab1.label.pack()

        
        #PREPROCESS TAB
        tab2.columnconfigure(0, weight=1)
        tab2.columnconfigure(1, weight=1)

        ##Config and dataset selector buttons
        ttk.Button(tab2, text="Select config", command=self.load_config_function).grid(column = 0, row = 0, padx = 10, pady = 10)
        ttk.Button(tab2, text="Select dataset", command=self.load_data_function).grid(column = 1, row = 0, padx = 10, pady = 10)

        ##Checkbox to disable augmentation
        self.no_augmentation_var = tk.BooleanVar()
        tab2.no_augmentation_checkbox = ttk.Checkbutton(tab2, text="Disable Augmentation", variable=self.no_augmentation_var)
        tab2.no_augmentation_checkbox.grid(row = 1, columnspan = 2, padx = 10, pady = 10)
        
        ##Button to start preprocessing
        ttk.Button(tab2, text="Preprocess", command=self.execute_command_pre).grid(row = 2, columnspan = 2, sticky=tk.S, padx = 10, pady = 10)

        #TRAIN TAB
        tab3.columnconfigure(0, weight=1)
        tab3.columnconfigure(1, weight=1)

        ##Config selector button
        ttk.Button(tab3, text="Select config", command=self.load_config_function).grid(row = 0, columnspan = 2, padx = 10, pady = 10)

        ##Select architecture - radio button
        ttk.Label(tab3, text="Select an option:").grid(row = 1, column = 0, rowspan = 2, padx=5, pady=5)
        global script_option_train
        script_option_train = tk.StringVar()
        option1 = ttk.Radiobutton(tab3, text="Diffusion", variable=script_option_train, value="tools/diffusion/train.py")
        option1.grid(row = 1, column = 1, padx = 5, pady = 5)
        option2 = ttk.Radiobutton(tab3, text="Hifisinger", variable=script_option_train, value="tools/hifisinger/train.py")
        option2.grid(row = 2, column = 1, padx = 5, pady = 5)

        ##Dropdown for training stage
        self.selected_option = tk.StringVar()


        self.option_menu = ttk.Combobox(tab3, textvariable = self.selected_option)  
        self.option_menu['values'] = ["Train from scratch", "Pretrain", "Resume"]
        self.option_menu['state'] = 'readonly'
        self.pretrain_var = tk.BooleanVar()
        self.resume_var = tk.BooleanVar()
        self.option_menu.grid(row = 3, column = 0, padx = 5, pady = 5)

        ##Button to select ckpt for pretrain/resume
        ttk.Button(tab3, text="Select ckpt", command=self.load_ckpt_function).grid(row = 3, column = 1, padx = 5, pady = 5)

        ##Checkbox to enable Tensorboard - UNTESTED
        self.tensorboard_var = tk.BooleanVar()
        tab3.tensorboard_checkbox = ttk.Checkbutton(tab3, text="Enable Tensorboard", variable=self.tensorboard_var)
        tab3.tensorboard_checkbox.grid(row = 4, columnspan = 2, padx = 5, pady = 5)

        ##Button to start training
        ttk.Button(tab3, text="Begin training", command=self.execute_command_train).grid(row = 5, columnspan = 2, padx = 5, pady = 5)

        #INFERENCE TAB

        ##Button to select ckpt AND config
        ttk.Button(tab4, text="Select model", command=self.load_model_function).grid(row = 0, columnspan = 2, padx = 5, pady = 5)

        ##Select architecture - radio button
        ttk.Label(tab4, text="Select an option:").grid(row = 1, column = 0, rowspan = 2, padx=5, pady=5)
        global script_option_inf
        script_option_inf = tk.StringVar()
        option1 = ttk.Radiobutton(tab4, text="Diffusion", variable=script_option_inf, value="tools/diffusion/inference.py")
        option1.grid(row = 1, column = 1, padx = 5, pady = 5)
        option2 = ttk.Radiobutton(tab4, text="Hifisinger", variable=script_option_inf, value="tools/hifisinger/inference.py")
        option2.grid(row = 2, column = 1, padx = 5, pady = 5)
        
        ##Enter speaker ID - default 0
        ttk.Label(tab4, text="Speaker:").grid(row = 3, column = 0, padx=5, pady=5)
        global speakerenter
        speakerenter = ttk.Entry(tab4)
        tab4.speakerenterbox = speakerenter
        tab4.speakerenterbox.insert(0, "0")
        tab4.speakerenterbox.grid(row = 3, column = 1, sticky = tk.E, padx=5, pady=5)
        
        ##Enter key change in semitones - default 0
        ttk.Label(tab4, text="Key change:").grid(row = 4, column = 0, padx=5, pady=5)
        global keyenter
        keyenter = ttk.Entry(tab4)
        tab4.keyenterbox = keyenter
        tab4.keyenterbox.insert(0, "0")
        tab4.keyenterbox.grid(row = 4, column = 1, sticky = tk.E, padx=5, pady=5)

        ##Checkbox to enable sampler interval/render speed - DIFFUSION ONLY
        self.speed_var = tk.BooleanVar()
        tab4.speed_checkbox = ttk.Checkbutton(tab4, text="Enable sampler interval", variable=self.speed_var)
        tab4.speed_checkbox.grid(row = 5, column = 0, sticky = tk.W, padx=5, pady=5)
        ##Enter sampler interval/render speed - default 20
        global speedval
        speedval = tk.Entry(tab4)
        tab4.speedenter = speedval
        tab4.speedenter.insert(0, "20")
        tab4.speedenter.grid(row = 5, column = 1, sticky = tk.E, padx=5, pady=5)

        ##Import/save buttons
        ttk.Button(tab4, text="Select input audio", command=self.load_input_function).grid(row = 6, column = 0, padx=5, pady=5)
        ttk.Button(tab4, text="Select export location", command=self.load_export_function).grid(row = 6, column = 1, padx=5, pady=5)

        ##Button to start inference
        ttk.Button(tab4, text="Inference", command=self.execute_command_inf).grid(row = 7, columnspan = 2, padx=5, pady=5)


    #define functions
    ##Selects config only
    def load_config_function(self):
        global configpath
        configpath = filedialog.askopenfilename(title="Select config file", initialdir="configs/", filetypes=[("Python files", "*.py")])
        print(configpath)

    ##Selects data folder
    def load_data_function(self):
        global datasetfolder
        datasetfolder = filedialog.askdirectory(title="Select dataset subfolder", initialdir="dataset/")
        print(datasetfolder)

    ##Runs preprocessing
    def execute_command_pre(self):
        if not configpath or not datasetfolder:
            self.label.config(text="Please select your config and the data you would like to preprocess first!")
            return

        cmd = ['python', 'tools/preprocessing/extract_features.py', '--config', configpath, '--path', datasetfolder, '--clean']
        if self.no_augmentation_var.get():
            cmd.append('--no-augmentation')
        output = subprocess.check_output(cmd, universal_newlines=True)
        print(output)

    ##Loads ckpt only
    def load_ckpt_function(self):
        global ckptpath
        ckptpath = filedialog.askopenfilename(title="Select ckpt File", filetypes=[("Checkpoint files", "*.ckpt")], initialdir = "checkpoints/")
        print(ckptpath)

    ##Runs training
    def execute_command_train(self):
        script_path_train = script_option_train.get()
        if script_path_train == "tools/diffusion/train.py":
            script_name = "diffusion"
        elif script_path_train == "tools/hifisinger/train.py":
            script_name = "hifisinger"
        else:
            raise ValueError("Invalid script path")
        print(script_path_train)
        if not configpath:
            self.label.config(text="Please select your config first!")
            return
        selected_option = self.selected_option.get()
        if selected_option == "Pretrain":
            self.pretrain_var.set(True)
            self.resume_var.set(False)
        elif selected_option == "Resume":
            self.pretrain_var.set(False)
            self.resume_var.set(True)
        else:
            self.pretrain_var.set(False)
            self.resume_var.set(False)

        # Construct the command
        cmd = ['python', script_path_train, '--config', configpath]
        if self.pretrain_var.get() == True:
            cmd.append('--pretrained')
        if self.resume_var.get() == True:
            cmd.append('--resume')
        if self.pretrain_var.get() == True or self.resume_var.get() == True:
            cmd.append(ckptpath)
        if self.tensorboard_var.get():
            cmd.append('--tensorboard')
        print(' '.join(cmd))
        output = subprocess.check_output(cmd, universal_newlines=True)
        print(output)

    ##Loads ckpt, then config
    def load_model_function(self):
        global ckpt_path
        ckpt_path = tk.filedialog.askopenfilename(title = "Select CKPT File", filetypes=[("Checkpoint files", "*.ckpt")], initialdir="checkpoints/")
        if ckpt_path == '':
            tk.messagebox.showerror("Error", "No CKPT file selected")
            return
        global cnfg_path
        cnfg_path = tk.filedialog.askopenfilename(title = "Select Config File", filetypes=[("Py files", "*.py")], initialdir="configs/")
        if cnfg_path == '':
            tk.messagebox.showerror("Error", "No config file selected")
            return
        
    ##Selects reference audio
    def load_input_function(self):
        global input_path
        input_path = tk.filedialog.askopenfilename(title = "Select WAV File", filetypes=[("WAV files", "*.wav")])
        if input_path == '':
            tk.messagebox.showerror("Error", "No WAV file selected")
            return

    ##Save as
    def load_export_function(self):
        global export_path
        export_path = tk.filedialog.asksaveasfilename(title = "Select WAV File", filetypes=[("WAV files", "*.wav")], defaultextension=".wav")
        if export_path == '':
            tk.messagebox.showerror("Error", "No WAV file selected")
            return

    ##Runs inference
    def execute_command_inf(self):
        script = script_option_inf.get()
        speaker = speakerenter.get()
        key = keyenter.get()
        speed = speedval.get()
        # Construct the command
        cmd = ['python', script, '--config', cnfg_path, '--checkpoint', ckpt_path, '--input', input_path, '--output', export_path, '--speaker', speaker, '--pitch_adjust', key]
        if self.speed_var.get():
            cmd.append('--sampler_interval')
            cmd.append(speed)
        print(' '.join(cmd))
        output = subprocess.check_output(cmd, universal_newlines=True)
        print(output)

if __name__ == "__main__":
    app = App()
    app.mainloop()
