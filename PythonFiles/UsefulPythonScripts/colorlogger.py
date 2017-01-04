header = '\033[95m'
info = '\033[94m'
darkgreen = '\033[92m'
warning = '\033[93m'
error = '\033[91m'
endc = '\033[0m'
yellowbg = '\033[43m'
purple = '\033[035m'
cyan = '\033[036m'
black = '\033[030m'
red = '\033[031m'
limegreen = '\033[032m'
yellow = '\033[033m'
blue = '\033[034m'
white = '\033[037m'
default = '\033[039m'
defaultbg = '\033[49m'
underline = '\033[4m'
italics = '\033[3m'
bold = '\033[1m'
inverse = '\033[7m'
reset = '\033[0m'
strike = '\033[9m'
blackbg = '\033[040m'
redbg = '\033[041m'
greenbg = '\033[042m'
bluebg = '\033[044m'
purplebg = '\033[045m'
cyanbg = '\033[046m'
whitebg = '\033[047m'


def log_warning(msg):
    print(warning + msg + reset)


def log_crit(msg):
    print(error + msg + reset)


def log_info(msg):
    print(info + msg + reset)


def log_highlight(msg):
    print(yellowbg + msg + reset)


def log(msg):
    print(msg + reset)


def block(bgcolor=redbg, txtcolor=red, text=''):
    print(f'{bgcolor}{txtcolor}{text}' + reset)


"""
Black       0;30     Dark Gray     1;30
Blue        0;34     Light Blue    1;34
Green       0;32     Light Green   1;32
Cyan        0;36     Light Cyan    1;36
Red         0;31     Light Red     1;31
Purple      0;35     Light Purple  1;35
Brown       0;33     Yellow        1;33
Light Gray  0;37     White         1;37
"""
