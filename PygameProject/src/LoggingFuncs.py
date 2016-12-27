import logging
import os


def log(message):
    path = 'logfile'
    comp_path = path + '/log.log'

    if not os.path.exists(path):
        os.mkdir(path)

    logging.basicConfig(filename=comp_path, level=logging.DEBUG)
    logging.log(logging.DEBUG, message)
