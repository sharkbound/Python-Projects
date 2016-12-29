import gui_funcs as gui
from enum_classes import GuiTextMode as text
from logger import *
from miscfuncs import *
from filefuncs import *


def main_logger():
    # clearlogs()
    # createlogfile()

    # logs = ['jim.log', 'bob.log', 'billy.log']
    logs = ['log.logsdfasfaf']
    index = 0

    for log in logs:
        prefixed = log
        log_i('Log file name pre-prefix: "{}" '.format(prefixed), file=prefixed)
        prefixed = prefixlogdir(log)
        logs[index] = prefixed
        log_i('Log file name post-prefix: "{}" '.format(prefixed), file=prefixed)
        index += 1

    # openlogfile(file='log.log')
    # openlogfile()

    for log in logs:
        openlogfile(log)

    sleep(3)

    # deletelogfile()
    # deletelogdir(log=False)
    # deletelogfile(file=log1)
    # deletelogfile(file=log2)
    deletelogdir(log=True, safemode=False)


def main_gui():
    gui.set_title('new title')
    gui.addtext_pack('testing text')
    gui.addtext_pack('testing \nagain \n:D')
    gui.startgui()


main_logger()
# main_gui()
