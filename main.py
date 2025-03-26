from tkinter import *
from settings import *
from widgets import *
import config

if __name__ == "__main__":
    config.main_window = Tk()
    window_settings(config.main_window)
    set_widgets(config.main_window)
    config.main_window.mainloop()