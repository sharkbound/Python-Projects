import time, guiTool, tkinter

from tkinter import Button
from memoryutils import *

gui = guiTool


def main():
    t1 = time.clock()
    printmemory()

    gui.set_width_height(200, 200)
    gui.addbtn("PIE")
    gui.set_title("Test title")
    gui.addtxt("testing test")
    gui.addchkbtn("checkbutton text")
    gui.mainloop()

    printmemory()
    t2 = time.clock()
    print(f'Execution time: \n\t{t2-t1}')


main()
