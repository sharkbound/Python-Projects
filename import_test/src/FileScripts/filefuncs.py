import os


def open(file, log=False):
    if os.path.exists(file):
        try:
            os.startfile(file)
        except Exception as e:
            if log:
                print('Failed to open file "{}":\n\t{}'.format(file, e))
    elif log:
        print('File "{}" does not exist!'.format(file))
