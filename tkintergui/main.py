import time, guiTool
from memoryutils import *

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

    # GUI()

    t2 = time.clock()
    print(f'Execution time: \n\t{t2-t1}')


main()
