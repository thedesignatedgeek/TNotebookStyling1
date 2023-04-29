from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *


# ===================================================
# Create a toplevel object and set it's size
# ===================================================
master = tk.Tk()
master.geometry("630x420")
master.resizable(0, 0)
master.title("TNotebook Style Demo")


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


# ===================================================
# Create an instance of the ttk.Notebook.  It's
#   parent is the "master" Toplevel object
# ===================================================
tn = ttk.Notebook(master)

# ===================================================
# Create four frames which will act as the container
#  area for the tabs.
# ===================================================
t1 = ttk.Frame(tn)
t2 = ttk.Frame(tn)
t3 = ttk.Frame(tn)
t4 = ttk.Frame(tn)

# ===================================================
#  Now add each frame into the Notebook
# ===================================================
tn.add(t1, text="Page 1")
tn.add(t2, text="Page 2")
tn.add(t3, text="Page 3")
tn.add(t4, text="Page 4")

# ===================================================
# Use place geometry manager to hold the Notebook
# Place it centered in the toplevel
# ===================================================
# Toplevel "630x420" whalf=315 hhalf=210 tnwhalf=151 tnhhalf=113
# tn.place(x=10, y=30, height=226, width=302, bordermode="ignore")
#
tn.place(x=164, y=97, height=226, width=302, bordermode="ignore")

# ===================================================
# apply the style to the notebook
# ===================================================
# setup_base_style()

# ===================================================
# Start the whole thing running
# ===================================================
master.mainloop()
