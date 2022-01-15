import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Mentor match")
        self.geometry("300x70")
        self.resizable(False, False)
