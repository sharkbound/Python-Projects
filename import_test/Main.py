from enum_classes import linemode
import gui_funcs as gui
from enum_classes import GuiTextMode as text
from logger import *
from miscfuncs import *
from filefuncs import *


def main_logger():
    clearlogs()
    createlogfile()

    logdir = log_file_dir

    openfile(logdir, log=True)

    # print('Log file contents: \n{}'.format(getlogfilecontents()))

    log_info('Filler log line...', endl_mode=linemode.space2)

    # values = list(getrange(2, includezero=False))
    # print(values)

    print('\nTrying to delete log directory...')
    deletelogdir(log=True)


def main_gui():
    gui.set_title('new title')
    gui.addtext_pack('testing text')
    gui.addtext_pack('testing again :D')
    gui.startgui()


# main_logger()
main_gui()
