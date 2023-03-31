import subprocess
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("Fish Training")

        self.load_config_button = tk.Button(master, text="Select config", command=self.load_config_function)
        self.load_config_button.pack()

        self.label = tk.Label(master, text="Select an option:")
        self.label.pack()

        self.script_options = [("Diffusion", "tools/diffusion/train.py"), ("Hifisinger", "tools/hifisinger/train.py")]
        self.selected_script = tk.StringVar()
        self.selected_script.set(self.script_options[0][1])

        for option, script_path in self.script_options:
            script_button = tk.Radiobutton(master, text=option, variable=self.selected_script, value=script_path)
            script_button.pack()

        self.options = ["Train from scratch", "Pretrain", "Resume"]
        self.selected_option = tk.StringVar()
        self.selected_option.set(self.options[0])

        self.option_menu = tk.OptionMenu(master, self.selected_option, *self.options)
        self.option_menu.pack()

        self.pretrain_var = tk.BooleanVar()
        self.resume_var = tk.BooleanVar()

        self.load_ckpt_button = tk.Button(master, text="Select ckpt", command=self.load_ckpt_function)
        self.load_ckpt_button.pack()

        self.tensorboard_var = tk.BooleanVar()
        self.tensorboard_checkbox = tk.Checkbutton(master, text="Enable Tensorboard", variable=self.tensorboard_var)
        self.tensorboard_checkbox.pack()

        self.execute_button = tk.Button(master, text="Begin training", command=self.execute_command)
        self.execute_button.pack()

    def load_config_function(self):
        global configpath
        configpath = filedialog.askopenfilename(title="Select CONFIG File", initialdir="configs/", filetypes=[("Python files", "*.py")])
        print(configpath)
        self.label.config(text="Config selected!")

    def load_ckpt_function(self):
        global ckptpath
        ckptpath = filedialog.askopenfilename(title="Select ckpt File", filetypes=[("Checkpoint files", "*.ckpt")])
        print(ckptpath)
        self.label.config(text="Checkpoint selected!")

    def execute_command(self):
        script_path = self.selected_script.get()
        if script_path == "tools/diffusion/train.py":
            script_name = "diffusion"
        elif script_path == "tools/hifisinger/train.py":
            script_name = "hifisinger"
        else:
            raise ValueError("Invalid script path")
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
        cmd = ['python', 'tools/diffusion/train.py', '--config', configpath]
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

root = tk.Tk()
my_gui = MyGUI(root)
root.mainloop()
