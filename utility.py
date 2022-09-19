import socket
import tkinter as tk
from tkinter import ttk


def connectedToInternet():
    try:
        socket.create_connection(
            ("www.google.com", 80)
        )  # better to set timeout as well
        return True
    except OSError:
        return False


def changeFrame(
    master: tk.Tk = None, oldFrame: ttk.Frame = None, newFrame: ttk.Frame = None
):
    print("Chaning frame")
    newFrame.tkraise()
