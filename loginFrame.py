import tkinter as tk
from tkinter import Label, ttk


class LoginFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        self.usernameLabel = Label(master=self, text="Username").grid(
            column=0, row=1, padx=5
        )
        self.username = tk.StringVar()
        self.usernameEntry = ttk.Entry(self, textvariable=self.username).grid(
            column=1, row=1
        )

        self.dobLabel = Label(master=self, text="D.O.B").grid(column=0, row=2, padx=5)
        self.dob = tk.StringVar()
        self.dobEntry = ttk.Entry(self, textvariable=self.dob).grid(column=1, row=2)

        ttk.Frame(master=self, height=20).grid(column=1, row=3)

        ttk.Button(master=self, text="Login").grid(column=0, row=4, columnspan=2)
