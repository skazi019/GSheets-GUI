import tkinter as tk
from tkinter import ttk
from loginFrame import LoginFrame


class HomeFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)

        ttk.Label(master=self, text="Role Change", font=("Helvetica", 24)).grid(
            column=1, row=1, pady=20
        )

        # Using frame as an empty box for proper widgets alignment
        ttk.Frame(master=self, height=50).grid(column=1, row=2)

        self._Frame = None
        self.switch_frame(frame_class=LoginFrame)

    def switch_frame(self, frame_class: ttk.Frame):
        new_frame = frame_class(self)
        if self._Frame is not None:
            self._Frame.destroy()
        self._Frame = new_frame
        self._Frame.grid(column=1, row=3)
