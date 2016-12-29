import logger
import gui_funcs as gui

from enum_classes import LineMode
from logger import log_info, createlogfile, deletelogdir, getlogfilecontents
from enum_classes import GuiTextMode as text
from miscfuncs import getrange


def main_logger():
    logger.clearlogs()
    createlogfile()

    logdir = logger.log_file_dir  # logger.log_file_dir.replace('/', '\\')

    # file.open(r'logs\log.log', log=True)

    print('Log file contents: \n{}'.format(getlogfilecontents()))

    log_info('testing log function', endl_mode=LineMode.space2)

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
