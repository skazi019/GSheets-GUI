import re
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from gSheets import GSheet

from updateDataFrame import UpdateDataFrame
from utility import connectedToInternet


class LoginFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.masterFrame: ttk.Frame = container
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        ttk.Label(master=self, text="Name").grid(column=0, row=1, padx=5)
        self.username = tk.StringVar()
        ttk.Entry(self, textvariable=self.username).grid(column=1, row=1)

        ttk.Frame(master=self, height=5).grid(column=1, row=2)

        ttk.Label(master=self, text="D.O.B").grid(column=0, row=3, padx=5)
        ttk.Label(master=self, text="(DD/MM/YYYY)", font=("", 8)).grid(
            column=0, row=4, padx=5
        )
        self.dob = tk.StringVar()
        ttk.Entry(self, textvariable=self.dob).grid(column=1, row=3, rowspan=2)

        ttk.Frame(master=self, height=20).grid(column=1, row=5)

        ttk.Button(
            master=self,
            text="Login",
            command=lambda: self.__switchToUpdateFrame(
                username=self.username.get(), dob=self.dob.get()
            ),
        ).grid(column=0, row=6, columnspan=2)

    def __switchToUpdateFrame(self, username: str, dob: str):
        if connectedToInternet():
            dataFlag, queryData = self.getSheetsData(username=username, dob=dob)

            if dataFlag == False:
                showerror(
                    title="Error in Data",
                    message="Error in fetching data.\nEither input was incorrect or data not present in the database.",
                )
            else:
                # passing data between frames using keyword arguements(**kwargs)
                self.masterFrame.switch_frame(
                    frame_class=UpdateDataFrame, queryData=queryData
                )
        else:
            showerror(
                title="Internet Connection Error",
                message="Please check your internet connection and try again",
            )

    def getSheetsData(self, username: str, dob: str):
        sheetData = GSheet().getSheet()
        sheetData = sheetData[
            (sheetData["Name"] == username) & (sheetData["DOB"] == dob)
        ]
        if len(sheetData) >= 1:
            return True, sheetData
        else:
            return False, pd.DataFrame()
