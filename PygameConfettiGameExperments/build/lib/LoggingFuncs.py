import logging
import os
import shutil
from datetime import datetime


def get_log_directory():
    return 'logfile'

def get_log_file_path():
    return '{}/log.log'.format(get_log_directory())

def create_log_folder():
    if not os.path.exists(get_log_directory()):
        os.mkdir(get_log_directory())

def delete_log_folder():
    if os.path.exists(get_log_directory()):
        import fileinput

        shutil.rmtree(get_log_directory(), False)


def format_time():
    now = datetime.now()
    return '{}:{}:{}'.format(now.hour, now.minute, now.second)


def format_date():
    now = datetime.now()
    return '{}/{}/{}'.format(now.month, now.day, now.year)


def log(message, logging_mode=logging.INFO):
    path = get_log_directory()
    comp_path = get_log_file_path()

    if not os.path.exists(path):
        os.mkdir(path)

    logging.basicConfig(filename=comp_path, level=logging_mode)
    logging.log(logging_mode, '[ {} {} ]: {}'.format(format_date(), format_time(), message))
