import gui_util, time, itertools

from memoryutils import *

gui = gui_util


def main():
    t1 = time.clock()
    printmemory()

    gui.set_width_height(200, 200)
    gui.addbtn("button name")
    gui.set_title("Test title")
    gui.addtxt("testing test")
    gui.addchkbtn("checkbutton text")
    gui.mainloop()

    printmemory()
    t2 = time.clock()
    print(f'Execution time: \n\t{t2-t1}')


main()
