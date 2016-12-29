from enum_classes import linemode
import gui_funcs as gui
from enum_classes import GuiTextMode as text
from logger import *
from miscfuncs import *
from filefuncs import *


def main_logger():
    # clearlogs()
    # createlogfile()

    logdir = log_file_dir

    log_i('Filler log line...')
    log_i('Filler log line...')

    openlogfile()
    sleep(2)
    deletelogdir(log=False)


def main_gui():
    gui.set_title('new title')
    gui.addtext_pack('testing text')
    gui.addtext_pack('testing \nagain \n:D')
    gui.startgui()


main_logger()
# main_gui()
