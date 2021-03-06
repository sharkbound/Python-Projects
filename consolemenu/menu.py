from typing import Dict, Callable

from .enums import MenuAction
from .util import chunk


class Menu:
    def __init__(self, **commands: Dict[str, Callable]):
        self.commands = commands
        self.commands['back'] = lambda *_: MenuAction.go_back

        self._register_local_commands()

    def _register_local_commands(self):
        for k, v in self.__class__.__dict__.items():
            if isinstance(v, named):
                self.commands[v.name] = v.func.__get__(self)
            elif k.startswith('do_') and callable(v):
                self.commands[k[3:]] = getattr(self, k)

    def show_command_options(self):
        if not self.commands:
            return

        print(f'available commands:')

        for cmds in chunk(self.commands, 5):
            print('\t'.join(c for c in cmds if c))

    def prompt(self):
        self.show_command_options()
        return input('\n>>> ')

    def lookup_command(self, raw, cmd, *args):
        return self.commands.get(cmd, lambda *a: None)

    def handle_input(self, raw, cmd, *args):
        return self.lookup_command(raw, cmd, *args)(cmd, *args)

    def pause(self):
        input('\npress enter to continue...\n')


class named:
    def __init__(self, name):
        self.name = name
        self.func = None

    def __call__(self, func):
        self.func = func
        return self
