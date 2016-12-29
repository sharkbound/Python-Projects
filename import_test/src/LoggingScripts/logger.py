import logging
import os
import shutil
import logging

from enum_classes import linemode
from datetime import datetime

log_dir = 'logs'
log_file_dir = r'logs\log.log'
log_file_name = 'log.log'


def log_info(msg, file=log_file_dir, endl_mode=linemode.newlinetab1, beforeprefixtab=False):
    createlogdir()
    logging.basicConfig(filename=file, level=logging.INFO)
    logging.log(logging.INFO, _get_prefix(add_tab=beforeprefixtab, endlinemode=endl_mode) + msg)


def createlogdir():
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)


def createlogfile(log=False):
    createlogdir()
    if not os.path.exists(log_file_dir):
        open(log_file_dir, 'a').close()
        if log:
            print('Created log file!')


def deletelogdir(log=False):
    if os.path.exists(log_dir):
        files = next(os.walk(log_dir))[2]
        dirs = next(os.walk(log_dir))[1]

        if len(files) == 1 and len(dirs) == 0:
            if files[0] == log_file_name:
                try:
                    shutil.rmtree(log_dir)
                    if log:
                        print('Deleted log directory!')
                except Exception as e:
                    print('\nSomething went wrong trying to delete the log directory! \n\tDetails: \n\t{}'.format(e))

def deletelogfile():
    if logfileexist():
        os.remove(log_file_dir)


def _get_prefix(add_tab=True, endlinemode=linemode.newlinetab1):
    now = datetime.now()
    params = [now.month, now.day, now.year, now.hour, now.minute, now.time().second]
    prefix = ''

    if add_tab:
        prefix = '\t[{}/{}/{} {}:{}:{}]:'.format(*params)
    else:
        prefix = '[{}/{}/{} {}:{}:{}]:'.format(*params)  # now.month, now.day, now.year, now.hour, now.minute)

    prefix = _append_endline(prefix, endlinemode)
    return prefix


def _append_endline(prefix, mode):
    if mode == linemode.newlinetab1:
        prefix += '\n\t'
    elif mode == linemode.newline:
        prefix += '\n'
    elif mode == linemode.newlinetab2:
        prefix += '\n\t\t'
    elif mode == linemode.tab1:
        prefix += '\t'
    elif mode == linemode.tab2:
        prefix += '\t\t'
    elif mode == linemode.space1:
        prefix += ' '
    elif mode == linemode.space2:
        prefix += '  '
    elif mode == linemode.space3:
        prefix += '   '

    return prefix


def getlogfilecontents():
    if logfileexist():
        file = open(log_file_dir)
        contents = file.read()
        file.close()
        return contents

def getlogfile():
    if logfileexist():
        return open(log_file_dir, 'w')
    else:
        return None

def logfileexist():
    return os.path.exists(log_file_dir)

def clearlogs():
    deletelogfile()
    createlogfile()
    # file = getlogfile()
    # if file != None:
    #     file.write('')
    #     file.close()
