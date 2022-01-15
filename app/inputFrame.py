import tkinter as tk
from tkinter import ttk, filedialog


class InputFrame(ttk.Frame):
    def __init__(self, container):
        super(InputFrame, self).__init__(container)
        options = {"padx": 5, "pady": 5}

        #  input label
        self.input_button = ttk.Button(self, text="Select folder")
        self.input_button["command"] = self.get_folder
        self.input_button.grid(column=2, row=0, sticky=tk.W, **options)

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def get_folder(self):
        folder = filedialog.askdirectory(
            title="Select folder with participant data", initialdir="/"
        )
        return folder
