from tkinter import *

def menu_bar(window):
    menubar = Menu(window)
    window.config(menu=menubar)
    #File Menu
    fileMenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=fileMenu)
    fileMenu.add_command(label="Open")
    fileMenu.add_command(label="Save")
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit")


def set_widgets(window):

    menu_bar(window)
    
    editor = Text(window,
                  bg="light yellow",
                  padx=5,
                  pady=5,
                  fg="black",
                  relief=FLAT,
                  borderwidth=0).pack(expand=True,fill='both')