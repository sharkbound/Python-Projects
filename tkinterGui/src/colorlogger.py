class colors:
    header = '\033[95m'
    info = '\033[94m'
    green = '\033[92m'
    warning = '\033[93m'
    error = '\033[91m'
    endc = '\033[0m'
    yellowbg = '\033[43m'
    purple = '\033[035m'
    cyan = '\033[036m'

    def disable(self):
        self.header = ''
        self.info = ''
        self.green = ''
        self.warning = ''
        self.error = ''
        self.endc = ''


def log_warning(msg):
    print(colors.warning + msg + colors.endc)


def log_crit(msg):
    print(colors.error + msg + colors.endc)


def log_info(msg):
    print(colors.info + msg + colors.endc)


def log_highlight(msg):
    print(colors.yellowbg + msg + colors.endc)


def log(msg, color=colors.info):
    print(color + msg + colors.endc)


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
