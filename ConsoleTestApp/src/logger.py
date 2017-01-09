import os
import shutil
from datetime import datetime

log_dir = 'logs\\'
log_file_dir = r'logs\log.log'
log_file_name = 'log.log'


# def log_info(msg, file=log_file_dir, endl_mode=linemode.newlinetab1, beforeprefixtab=False):
#     createlogdir()
#     logging.basicConfig(filename=file, level=logging.INFO)
#     logging.log(logging.INFO, _get_prefix(add_tab=beforeprefixtab, endlinemode=endl_mode) + msg)

# prefixes filesname with logs\ if it doesnt already have in the name, unlike logtofile()
# which does not add the log directory as a file path prefix
def log(msg, file=log_file_dir, tag=' [INFO]:  ', consolelog=False):
    file = prefixlogdir(file)
    createlogfile(file=file)

    with open(file, 'a') as lf:
        lf.writelines(_get_datetime_prefix() + tag + msg + '\n')

    if consolelog:
        print(f'Added text: "{msg}" to file: "{file}"')


# logtofile does not prefix the filename with logs\ like log() does
def logtofile(msg, file=log_file_dir, tag=' [INFO]:  '):
    createlogdir()

    with open(file, 'a') as lf:
        lf.writelines(_get_datetime_prefix() + tag + msg + '\n')


def createlogdir():
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)


def createlogfile(file=log_file_dir, log=False):
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


def deletelogdir(safemode=True, log=False):
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
                            f'\nSomething went wrong trying to delete the log directory! \n\tDetails: \n\t{e}')
                else:
                    if log:
                        print(f'Not deleting log dir because file name is {files[0]} and not log.log')
            else:
                if log:
                    print(f'Not deleting log dir because file count is: {len(files)}, and dir count is: {len(dirs)}')
        else:
            try:
                shutil.rmtree(log_dir)
                if log:
                    print('Deleted log directory!')
            except Exception as e:
                print(f'\nSomething went wrong trying to delete the log directory! \n\tDetails: \n\t{e}')


def deletelogfile(file=log_file_dir):
    file = prefixlogdir(file)
    if logfileexist(file=file):
        os.remove(file)


def _get_datetime_prefix():
    now = datetime.now()
    return  f'[{now.month}/{now.day}/{now.year} {now.hour}:{now.minute}:{now.second}]'


def getlogfilecontents(file = log_file_dir, prefix = True):
    if logfileexist():
        if prefix:
            file = prefixlogdir(file)

        with open(file) as lf:
            contents = lf.read()

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


def launchlogfile(file=log_file_dir, prefixfile=True, log=False):
    if prefixfile:
        file = prefixlogdir(file)
    if logfileexist(file=file):
        try:
            os.startfile(file)
        except:
            if log:
                print('Error attempting to open file {}'.format(file))

                # def _get_endl(endlinemode=linemode.space2):
                #     prefix = _append_endline(endlinemode)
                #     return prefix
                #
                #
                # def _append_endline(mode, text=''):
                #     if mode == linemode.newlinetab1:
                #         text += '\n\t'
                #     elif mode == linemode.newline:
                #         text += '\n'
                #     elif mode == linemode.newlinetab2:
                #         text += '\n\t\t'
                #     elif mode == linemode.tab1:
                #         text += '\t'
                #     elif mode == linemode.tab2:
                #         text += '\t\t'
                #     elif mode == linemode.space1:
                #         text += ' '
                #     elif mode == linemode.space2:
                #         text += '  '
                #     elif mode == linemode.space3:
                #         text += '   '
                #
                #     return text
