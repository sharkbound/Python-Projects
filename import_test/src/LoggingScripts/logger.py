import logging
import os
import shutil
import logging

from enum_classes import linemode
from datetime import datetime

log_dir = 'logs\\'
log_file_dir = r'logs\log.log'
log_file_name = 'log.log'


# def log_info(msg, file=log_file_dir, endl_mode=linemode.newlinetab1, beforeprefixtab=False):
#     createlogdir()
#     logging.basicConfig(filename=file, level=logging.INFO)
#     logging.log(logging.INFO, _get_prefix(add_tab=beforeprefixtab, endlinemode=endl_mode) + msg)


def log_i(msg, file=log_file_dir, tag=' [INFO]: ', consolelog=True):
    file = prefixlogdir(file)
    createlogfile(file=file)
    compmsg = _get_datetime_prefix() + tag + msg + '\n'
    lf = open(file, 'a')
    lf.writelines(compmsg)
    lf.close()
    if consolelog:
        print('Added text: "{}" to file: "{}"'.format(msg, file))


def logtofile(msg, file=log_file_dir, tag=' [INFO]: '):
    createlogdir()
    createlogfile()
    compmsg = _get_datetime_prefix() + tag + msg + '\n'
    lf = open(file, 'a')
    lf.writelines(compmsg)
    lf.close()


def createlogdir():
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)


def createlogfile(log=False, file=log_file_dir):
    createlogdir()
    file = prefixlogdir(file)
    if not os.path.exists(file):
        open(file, 'a').close()
        if log:
            print('Created log file!')


def prefixlogdir(file):
    if file != log_file_dir and not file.__contains__(log_dir):
        file = log_dir + file
    return file


def deletelogdir(log=False, safemode=True):
    if os.path.exists(log_dir):
        if safemode:
            files = next(os.walk(log_dir))[2]
            dirs = next(os.walk(log_dir))[1]

            if len(files) == 1 and len(dirs) == 0:
                if files[0] == log_file_name:
                    try:
                        shutil.rmtree(log_dir)
                        if log:
                            print('Deleted log directory!')
                    except Exception as e:
                        print(
                            '\nSomething went wrong trying to delete the log directory! \n\tDetails: \n\t{}'.format(e))
                else:
                    if log:
                        print('Not deleting log dir because file name is {} and not log.log'.format(files[0]))
            else:
                if log:
                    print('Not deleting log dir because file count is: {}, and dir count is: {}'.format(len(files),
                                                                                                        len(dirs)))
        else:
            try:
                shutil.rmtree(log_dir)
                if log:
                    print('Deleted log directory!')
            except Exception as e:
                print('\nSomething went wrong trying to delete the log directory! \n\tDetails: \n\t{}'.format(e))


def deletelogfile(file=log_file_dir):
    file = prefixlogdir(file)
    if logfileexist(file=file):
        os.remove(file)


def _get_datetime_prefix():
    now = datetime.now()
    params = [now.month, now.day, now.year, now.hour, now.minute, now.time().second]
    prefix = ''
    prefix = '[{}/{}/{} {}:{}:{}]'.format(*params)
    return prefix


def _get_endl(endlinemode=linemode.space2):
    prefix = _append_endline(endlinemode)
    return prefix


def _append_endline(mode, text=''):
    if mode == linemode.newlinetab1:
        text += '\n\t'
    elif mode == linemode.newline:
        text += '\n'
    elif mode == linemode.newlinetab2:
        text += '\n\t\t'
    elif mode == linemode.tab1:
        text += '\t'
    elif mode == linemode.tab2:
        text += '\t\t'
    elif mode == linemode.space1:
        text += ' '
    elif mode == linemode.space2:
        text += '  '
    elif mode == linemode.space3:
        text += '   '

    return text


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


def logfileexist(file=log_file_dir):
    return os.path.exists(file)


def clearlogs():
    deletelogfile()
    createlogfile()
    # file = getlogfile()
    # if file != None:
    #     file.write('')
    #     file.close()
