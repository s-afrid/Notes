import config
from widgets import *

def bind_keys(window):
    window.bind("<Control-n>", lambda event: new_file())
    window.bind("<Control-o>", lambda event: open_file())
    window.bind("<Control-s>", lambda event: save_file())
    window.bind("<Control-Shift-S>", lambda event: save_as_file())
    window.bind("<Control-q>", lambda event: config.main_window.destroy())
    window.bind("<Control-Shift-C>",lambda event: new_file())
    window.bind("<Control-z>",lambda event : undo())
    window.bind("<Control-a>",lambda event : redo())
    window.bind("<Control-v>",lambda event : paste())
    window.bind("<Control-c>",lambda event : copy())