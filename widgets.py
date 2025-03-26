from tkinter import *
from tkinter import filedialog
import config


def open_file():
    file_path = filedialog.askopenfile()
    config.main_window.title(file_path.name)
    with open(file_path.name) as file:
        content = file.read()
        editor.insert(1.0,content)
        file.close()
        


def menu_bar(window):
    menubar = Menu(window)
    window.config(menu=menubar)
    #File Menu
    fileMenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=fileMenu)
    fileMenu.add_command(label="Open File",command=open_file)
    fileMenu.add_command(label="Save File")
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit")


def set_widgets(window):

    menu_bar(window)
    global editor
    editor = Text(window,
                  bg="light yellow",
                  padx=5,
                  pady=5,
                  fg="black",
                  relief=FLAT,
                  borderwidth=0)
    editor.pack(expand=True,fill='both')
    