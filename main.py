import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, showwarning

from homeFrame import HomeFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("RoleChange")
        # self.geometry("300x120")
        # self.resizable(False, False)
        window_width = 640
        window_height = 320

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        self.resizable(width=False, height=True)

        # Default frame to show
        homeFrame = HomeFrame(self)
        homeFrame.pack()


app = App()
app.mainloop()
