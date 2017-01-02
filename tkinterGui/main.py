import time, guiTool, tkinter, misc
from tkinter import Button
from memoryutils import *
from misc import rep_func as rep
from colorlogger import log_warning, colors as c, log_crit, log_info, log, log_highlight

# from colors import bcolors as color

gui = guiTool


def addnums(n1, n2):
    print(n1 + n2)


def GUI():
    gui.set_width_height(200, 200)
    gui.addbtn("PIE")
    gui.set_title("Test title")
    gui.addlabel("testing test")
    gui.addchkbtn("checkbutton text")
    gui.mainloop()


def main():
    t1 = time.clock()

    printmemory()

    GUI()

    t2 = time.clock()
    print(f'Execution time: \n\t{t2-t1}')


main()
