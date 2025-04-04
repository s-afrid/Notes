from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
import pyperclip
import config

#File functions
def open_file():   
    config.file_path = filedialog.askopenfile()
    config.main_window.title(config.file_path.name)
    with open(config.file_path.name) as file:
        content = file.read()
        config.editor.insert(1.0,content)
        file.close()       
def save_file():
    if config.file_path != None:
        config.main_window.title(config.file_path.name)
        with open(config.file_path.name,'w') as file:
            content = config.editor.get(1.0,END)
            file.write(content)
            file.close()
    else:
        save_as_file()
def save_as_file():
    config.file_path = filedialog.asksaveasfile(defaultextension=".txt",
                                                filetypes=[('Text',".txt"),('All Files',".*")])

    if config.file_path is None:
        return
    else:
        config.main_window.title(config.file_path.name)
        filetext = config.editor.get(1.0,END)
        config.file_path.write(filetext)
        config.file_path.close()
def new_file():
    if config.file_path != None:
        config.file_path.close()
        config.editor.delete(1.0,END)
        config.main_window.title("Notes")
        config.file_path = None
# Undo/Redo function    
def undo():
    config.redo.append(config.editor.get("end-2c"))
    config.editor.delete("end-2c")  
def redo():
    config.editor.insert(END,config.redo.pop())
# Copy/Paste function
def paste():
    clipboard_text = pyperclip.paste()
    config.editor.insert("end",clipboard_text)
def copy():
    if config.editor.tag_ranges(SEL):
        selected_text = config.editor.get(SEL_FIRST, SEL_LAST)
        pyperclip.copy(selected_text)
    else:
        pyperclip.copy(config.editor.get(1.0,END))

# Font functions
def font_color():
    color = colorchooser.askcolor()
    colorhex = color[1]
    config.editor.config(fg=colorhex)

def menu_bar(window):
    menubar = Menu(window)
    window.config(menu=menubar)
    #File Menu
    fileMenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=fileMenu)
    fileMenu.add_command(label="New",accelerator="Ctrl+N",command=new_file)
    fileMenu.add_command(label="Open",accelerator="Ctrl+O",command=open_file)
    fileMenu.add_command(label="Save",accelerator="Ctrl+S",command=save_file)
    fileMenu.add_command(label="Save As",accelerator="Ctrl+Shift+S",command=save_as_file)
    fileMenu.add_command(label="Close",accelerator="Ctrl+Shift+C",command=lambda : new_file())
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit",accelerator="Ctrl+Q",command=lambda : config.main_window.destroy())
    #Edit Menu
    editMenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit",menu=editMenu)
    editMenu.add_command(label="Undo",accelerator="Ctrl+Z",
                         command=undo)
    editMenu.add_command(label="Redo",accelerator="Ctrl+A",
                        command=redo)
    editMenu.add_command(label="Copy",accelerator="Ctrl+C",
                         command=copy)
    editMenu.add_command(label="Paste",accelerator="Ctrl+V",
                        command=paste)
    editMenu.add_separator()
    editMenu.add_command(label="Font Color",command=font_color)
    


def set_widgets(window):

    menu_bar(window)
    config.editor = Text(window,
                  bg="light yellow",
                  padx=5,
                  pady=5,
                  fg="black",
                  relief=FLAT,
                  borderwidth=0)
    config.editor.pack(expand=True,fill='both')
    