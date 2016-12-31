import gui_util, time, itertools

from memoryutils import *

gui = gui_util


def main():
    t1 = time.clock()

    gui.set_title("Test title")
    gui.packtxt("testing test")
    gui.mainloop()

    t2 = time.clock()
    print(f'Execution time: \n\t{t2-t1}')


main()
