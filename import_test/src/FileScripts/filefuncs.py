import os
from logger import log_file_dir
import subprocess
from subprocess import check_output
from logger import prefixlogdir


def openfile(file, log=False):
    if os.path.exists(file):
        try:
            return os.startfile(file)
        except Exception as e:
            if log:
                print('Failed to open file "{}":\n\t{}'.format(file, e))
    elif log:
        print('File "{}" does not exist!'.format(file))


def openlogfile(file=log_file_dir):
    # notepadproc = openfile(log_file_dir, log=True)
    # print(notepadproc)
    file=prefixlogdir(file)
    openfile(file, log=True)


def killproc(procname):
    proc = subprocess.Popen(procname)
    proc.kill()


def killnotepad():
    # killproc('notepad++.exe')
    print('Pid: ' + str(get_pid('notepad++.exe')))


def _getpid(procname):
    return check_output(["pidof", procname])


def get_pid(name):
    return check_output(["pidof", name])
