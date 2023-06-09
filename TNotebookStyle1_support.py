#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Apr 28, 2023 12:42:44 PM CDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import TNotebookStyle1

_debug = True  # False to eliminate debug printing from callback functions.


def main(*args):
    """Main entry point for the application."""
    global root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = TNotebookStyle1.Toplevel1(_top1)
    startup()
    root.mainloop()


def startup():
    setup_base_style()
    # _w1.TNotebook1.config(background=)


def setup_base_style():
    global debug
    # ===================================================
    # Sets up a base style for the TNotebook.
    #   I blatently stole this from Don and hacked it to make it work
    #   for me.  You can use this as a guide to make your own.
    # ===================================================
    style = ttk.Style()

    style.map(
        "TNotebook.Tab",
        background=[
            ("selected", "gray54"),
            ("active", "gray86"),
            ("!active", "sandybrown"),
        ],
        foreground=[("selected", "white"), ("active", "black"), ("!active", "black")],
    )


if __name__ == "__main__":
    TNotebookStyle1.start_up()
