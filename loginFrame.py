import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

from utility import connectedToInternet


class LoginFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        self.usernameLabel = ttk.Label(master=self, text="Username").grid(
            column=0, row=1, padx=5
        )
        self.username = tk.StringVar()
        self.usernameEntry = ttk.Entry(self, textvariable=self.username).grid(
            column=1, row=1
        )

        self.dobLabel = ttk.Label(master=self, text="D.O.B").grid(
            column=0, row=2, padx=5
        )
        self.dob = tk.StringVar()
        self.dobEntry = ttk.Entry(self, textvariable=self.dob).grid(column=1, row=2)

        ttk.Frame(master=self, height=20).grid(column=1, row=3)

        ttk.Button(
            master=self,
            text="Login",
            command=lambda: self.__getSheetsData(
                username=self.username.get(), dob=self.dob.get()
            ),
        ).grid(column=0, row=4, columnspan=2)

    def __getSheetsData(self, username: str, dob: str):
        if connectedToInternet():
            # TODO: get the data from google sheets and show in a frame
            # swtich to that frame and allow for updates
            showinfo(
                title="Success",
                message=f"Getting sheets data for\nUsername: {username}\nDOB:{dob}",
            )
        else:
            showerror(
                title="Internet Connection Error",
                message="Please check your internet connection and try again",
            )
