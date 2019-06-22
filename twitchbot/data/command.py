from typing import List


class Command:
    def __init__(self, func, name, help=None, permission=None):
        self.func = func
        self.name = name
        self.help = help or ''
        self.permission = permission or ''

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)

    def __repr__(self):
        return f'<Command: {self.name}>'


def command(name=None, help=None, permission=None):
    def _command(func):
        cmd = Command(func, name or func.__name__, help, permission)
        commands.append(cmd)
        return cmd

    return _command


commands: List[Command] = []
