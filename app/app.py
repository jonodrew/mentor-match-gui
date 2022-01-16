import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Mentor match")
        self.geometry("300x140")
        self.resizable(True, True)
