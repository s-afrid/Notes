from tkinter import *

def set_widgets(window):
    
    editor = Text(window,
                  bg="light yellow",
                  padx=5,
                  pady=5,
                  fg="black",height=400,
                  relief=FLAT,
                  borderwidth=0).pack(side=RIGHT)
    directory = Listbox(window,
                        bg="light blue",
                        height=400,
                        relief=FLAT,
                        borderwidth=0).pack(side=LEFT)