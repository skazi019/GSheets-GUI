import pandas as pd
import tkinter as tk
from tkinter import Label, ttk


class UpdateDataFrame(ttk.Frame):
    def __init__(self, container: ttk.Frame, queryData: pd.DataFrame):
        super().__init__(container)
        self.masterFrame: ttk.Frame = container
        self._queryData: pd.DataFrame = queryData

        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        # Using frame as an empty box for proper widgets alignment
        # ttk.Frame(master=self, height=20).grid(column=0, columnspan=2, row=2)

        ttk.Label(master=self, text="Name").grid(column=0, row=1, padx=5)
        ttk.Label(master=self, text=self._queryData["Name"].values[0]).grid(
            column=1, row=1, padx=5
        )

        ttk.Label(master=self, text="D.O.B").grid(column=0, row=2, padx=5)
        ttk.Label(master=self, text=self._queryData["DOB"].values[0]).grid(
            column=1, row=2, padx=5
        )

        ttk.Frame(master=self, height=50).grid(column=1, row=3)

        # Importing here to handle the circular import error
        from loginFrame import LoginFrame

        ttk.Button(
            master=self,
            text="back to Home",
            command=lambda: self.masterFrame.switch_frame(frame_class=LoginFrame),
        ).grid(column=0, row=4, columnspan=2)
