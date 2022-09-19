import tkinter as tk
from tkinter import Label, ttk
from loginFrame import LoginFrame


class HomeFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        ttk.Label(master=self, text="Role Change", font=("Helvetica", 24)).grid(
            column=1, row=1, pady=20
        )

        # Using frame as an empty box for proper widgets alignment
        ttk.Frame(master=self, height=50).grid(column=1, row=2)

        loginFrame = LoginFrame(self)
        loginFrame.grid(column=1, row=3)
