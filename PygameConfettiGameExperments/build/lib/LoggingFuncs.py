import logging
import os
import shutil

from datetime import datetime
from os.path import exists
from os import mkdir, getcwd, walk

log_file_name = 'log.log'
log_file_name_with_ext = r'\log.log'


def get_files_in_dir(dir):
    if exists(dir):
        return next(walk(dir))[2]  # walk get all roots, directories, and files from
        # a path given and put it into 3 separate list for each [0] is roots, [1] is directories, [2] is files


def get_child_dirs(dir):
    if exists(dir):
        return next(walk(dir))[1]


def log_dir_exist():
    return exists(get_log_directory_complete())

def log_file_exist():
    return exists(get_log_file_path_complete())


def get_log_directory_name():
    return 'logfile'


def get_log_directory_path():
    return r'\logfile'


def get_log_directory_complete():
    return getcwd() + get_log_directory_path()


def get_log_file_path():
    return '{}\log.log'.format(get_log_directory_name())


def get_log_file_path_complete():
    return '{}\log.log'.format(get_log_directory_complete())


def create_log_folder():
    if not log_dir_exist():
        mkdir(get_log_directory_complete())


def create_log_file():
    if not log_dir_exist():
        mkdir(get_log_directory_complete())

    if not exists(get_log_file_path_complete()):
        open(get_log_file_path_complete(), 'a').close()
        # print('created log file!')


def delete_log_folder():
    if os.path.exists(get_log_directory_complete()):
        files = get_files_in_dir(get_log_directory_complete())

        if len(files) == 1 and len(get_child_dirs(get_log_directory_complete())) == 0:
            if files[0] == log_file_name:
                shutil.rmtree(get_log_directory_name(), False)


def format_time():
    now = datetime.now()
    return '{}:{}:{}'.format(now.hour, now.minute, now.second)


def format_date():
    now = datetime.now()
    return '{}/{}/{}'.format(now.month, now.day, now.year)


def log(message, logging_mode=logging.INFO):
    path = get_log_directory_name()
    comp_path = get_log_file_path()

    if not os.path.exists(path):
        os.mkdir(path)

    logging.basicConfig(filename=comp_path, level=logging_mode)
    logging.log(logging_mode, '[ {} {} ]: {}'.format(format_date(), format_time(), message))
