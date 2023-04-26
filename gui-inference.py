import subprocess
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("Fish Inference")

        ##SELECT MODEL##
        self.load_model_button = tk.Button(master, text="Select model", command=self.load_model_function)
        self.load_model_button.pack()


        ##SELECT ARCHITECTURE##
        self.label = tk.Label(master, text="Select an option:")
        self.label.pack()

        self.script_options = [("Diffusion", "tools/diffusion/inference.py"), ("Hifisinger", "tools/hifisinger/inference.py")]
        self.selected_script = tk.StringVar()
        self.selected_script.set(self.script_options[0][1])

        for option, script_path in self.script_options:
            script_button = tk.Radiobutton(master, text=option, variable=self.selected_script, value=script_path)
            script_button.pack()


        ##MULTISPEAKER##
        self.label = tk.Label(master, text="Speaker:")
        self.label.pack()
        
        self.speakerenter = tk.Entry(master, textvariable=tk.StringVar(value="0"))
        self.speakerenter.pack()


        ##KEY##
        self.label = tk.Label(master, text="Key change:")
        self.label.pack()
        
        self.keyenter = tk.Entry(master, textvariable=tk.StringVar(value="0"))
        self.keyenter.pack()


        ##INTERVAL##
        self.speed_var = tk.BooleanVar()
        self.speed_checkbox = tk.Checkbutton(master, text="Enable sampler interval", variable=self.speed_var)
        self.speed_checkbox.pack()
        
        self.speedenter = tk.Entry(master, textvariable=tk.StringVar(value="20"))
        self.speedenter.pack()


        ##INPUT##
        self.load_input_button = tk.Button(master, text="Select input audio", command=self.load_input_function)
        self.load_input_button.pack()


        ##OUTPUT##
        self.load_export_button = tk.Button(master, text="Select export location", command=self.load_export_function)
        self.load_export_button.pack()


        ##EXECUTE##
        self.execute_button = tk.Button(master, text="Inference", command=self.execute_command)
        self.execute_button.pack()
    
    def load_model_function(self):
        global ckpt_path
        ckpt_path = tk.filedialog.askopenfilename(title = "Select CKPT File", filetypes=[("Checkpoint files", "*.ckpt")])
        if ckpt_path == '':
            tk.messagebox.showerror("Error", "No CKPT file selected")
            return
        global cnfg_path
        cnfg_path = tk.filedialog.askopenfilename(title = "Select Config File",filetypes=[("Py files", "*.py")])
        if cnfg_path == '':
            tk.messagebox.showerror("Error", "No config file selected")
            return
        
    def load_input_function(self):
        global input_path
        input_path = tk.filedialog.askopenfilename(title = "Select WAV File", filetypes=[("WAV files", "*.wav")])
        if input_path == '':
            tk.messagebox.showerror("Error", "No WAV file selected")
            return

    def load_export_function(self):
        global export_path
        export_path = tk.filedialog.asksaveasfilename(title = "Select WAV File", filetypes=[("WAV files", "*.wav")], defaultextension=".wav")
        if export_path == '':
            tk.messagebox.showerror("Error", "No WAV file selected")
            return

    def execute_command(self):
        speaker = self.speakerenter.get()
        key = self.keyenter.get()
        speed = self.speedenter.get()
        script_path = self.selected_script.get()
        if script_path == "tools/diffusion/inference.py":
            script_name = "diffusion"
        elif script_path == "tools/hifisinger/inference.py":
            script_name = "hifisinger"
        else:
            raise ValueError("Invalid script path")
            return


        # Construct the command
        cmd = ['python', script_path, '--config', cnfg_path, '--checkpoint', ckpt_path, '--input', input_path, '--output', export_path, '--speaker', speaker, '--pitch_adjust', key]
        if self.speed_var.get():
            cmd.append('--sampler_interval')
            cmd.append(speed)
        print(' '.join(cmd))
        output = subprocess.check_output(cmd, universal_newlines=True)
        print(output)

root = tk.Tk()
my_gui = MyGUI(root)
root.mainloop()

