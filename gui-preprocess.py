import subprocess
import tkinter as tk
from tkinter import filedialog

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("Fish Preprocessing")

        self.label = tk.Label(master, text="Select your config and the data you would like to preprocess.")
        self.label.pack()

        self.load_model_button = tk.Button(master, text="Select config and data to preprocess", command=self.load_model_function)
        self.load_model_button.pack()

        self.no_augmentation_var = tk.BooleanVar()
        self.no_augmentation_checkbox = tk.Checkbutton(master, text="Disable Augmentation", variable=self.no_augmentation_var)
        self.no_augmentation_checkbox.pack()

        self.execute_button = tk.Button(master, text="Preprocess", command=self.execute_command)
        self.execute_button.pack()


    def load_model_function(self):
        global configpath
        global datasetfolder
        configpath = filedialog.askopenfilename(title="Select CONFIG File", initialdir="configs/", filetypes=[("Python files", "*.py")])
        print(configpath)
        datasetfolder = filedialog.askdirectory(title="Select Dataset Subfolder", initialdir="dataset/")
        print(datasetfolder)
        self.label.config(text="Config and data selected!")

    def execute_command(self):
        if not configpath or not datasetfolder:
            self.label.config(text="Please select your config and the data you would like to preprocess first!")
            return

        cmd = ['python', 'tools/preprocessing/extract_features.py', '--config', configpath, '--path', datasetfolder, '--clean']
        if self.no_augmentation_var.get():
            cmd.append('--no-augmentation')
        output = subprocess.check_output(cmd, universal_newlines=True)
        print(output)

root = tk.Tk()
my_gui = MyGUI(root)
root.mainloop()
