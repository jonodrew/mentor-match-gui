import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.constants import DISABLED, NORMAL
from matching.process import conduct_matching_from_file
import pathlib
import functools


class InputFrame(ttk.Frame):
    def __init__(self, container):
        super(InputFrame, self).__init__(container)
        options = {"padx": 5, "pady": 5}
        self.directory_path = ""

        #  input label
        self.input_button = ttk.Button(self, text="Select folder")
        self.input_button["command"] = self.get_folder
        self.input_button.grid(column=2, row=0, sticky=tk.W, **options)

        self.process_button = ttk.Button(self, text="Start processing")
        self.process_button["state"] = DISABLED
        self.process_button.grid(column=2, row=4, sticky=tk.W, **options)

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def get_folder(self):
        folder = filedialog.askdirectory(
            title="Select folder with participant data", initialdir="/"
        )
        self.directory_path = folder
        self.process_button["state"] = NORMAL
        self.process_button["command"] = functools.partial(
            conduct_matching_from_file, pathlib.Path(self.directory_path)
        )
