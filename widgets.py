from tkinter import *
from tkinter import filedialog
import config

def open_file():   
    config.file_path = filedialog.askopenfile()
    config.main_window.title(config.file_path.name)
    with open(config.file_path.name) as file:
        content = file.read()
        editor.insert(1.0,content)
        file.close()
        
def save_file():
    if config.file_path != None:
        config.main_window.title(config.file_path.name)
        with open(config.file_path.name,'w') as file:
            content = editor.get(1.0,END)
            file.write(content)
            file.close()
    else:
        save_as_file()

def save_as_file():
    config.file_path = filedialog.asksaveasfile(defaultextension=".txt",filetypes=[('Text',".txt"),('All Files',".*")])
    filetext = editor.get(1.0,END)
    config.file_path.write(filetext)
    config.file_path.close()
    if config.file_path is None:
        return
    else:
        config.main_window.title(config.file_path.name)

def new_file():
    if config.file_path != None:
        config.file_path.close()
        editor.delete(1.0,END)
        config.main_window.title("Notes")
        config.file_path = None


def menu_bar(window):
    menubar = Menu(window)
    window.config(menu=menubar)
    #File Menu
    fileMenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=fileMenu)
    fileMenu.add_command(label="New",command=new_file)
    fileMenu.add_command(label="Open",command=open_file)
    fileMenu.add_command(label="Save",command=save_file)
    fileMenu.add_command(label="Save As",command=save_as_file)
    fileMenu.add_command(label="Close",command=lambda : new_file())
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit",command=lambda : config.main_window.destroy())
    #Edit Menu
    editMenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit",menu=editMenu)
    editMenu.add_command(label="Undo")
    editMenu.add_command(label="Copy")
    editMenu.add_command(label="Paste")


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
    