import traceback
from collections import defaultdict
from inspect import ismethod, isfunction
from typing import List, Dict, Callable, Union, Any, DefaultDict
from shlex import split


def _parse_cmd(text):
    try:
        v = split(text)
    except:
        v = text.split(' ')
    return v


class command:
    """
    usage:

    >>> class MyScreen(Screen):
    >>>     @command('version')
    >>>     def version(self, *args):
    >>>         # code
    or:
    >>> class MyScreen(Screen):
    >>>     @command
    >>>     def version(self, *args):
    >>>         # code
    """

    func: Callable[[List[str]], None]

    def __init__(self, name_or_func, desc: str = 'no description'):
        self.desc = desc
        if isfunction(name_or_func) or ismethod(name_or_func):
            self.func = name_or_func
            self.name = name_or_func.__name__
        else:
            self.name = name_or_func
            self.func = lambda *_, **__: None

    def execute(self, *args):
        self.func(*args)

    def __call__(self, func):
        self.func = func
        return self


class Screen:
    id: str
    name: str = 'MISSING NAME'
    mgr: 'ScreenManager' = None
    cmds: Dict[str, command]

    def __init_subclass__(cls, **kwargs):
        if cls.__init__.__code__.co_argcount == 1:
            cls.mgr.screens[cls.id] = cls()

    def __init__(self):
        self.cmds = {}
        self._find_cmds()

    def _find_cmds(self):
        for k, v in tuple(self.__class__.__dict__.items()):
            if isinstance(v, command):
                # we need to bind the function to the instance,
                # manually calling __get__ on the function does this
                v.func = v.func.__get__(self)
                self.cmds[v.name.lower()] = v

    def pause(self):
        input('\npress enter to continue...')

    def can_enter(self, prev: 'Screen'):
        return True

    def can_leave(self, dest: 'Screen'):
        return True

    def on_enter(self):
        pass

    def on_leave(self):
        pass

    def on_leave_denied(self, dest: 'Screen'):
        pass

    def on_enter_denied(self, prev: 'Screen'):
        pass

    @property
    def options(self):
        return 'options:\n\t' + '\n\t'.join(f'{cmd.name} - {cmd.desc}' for cmd in self.cmds.values())

    @property
    def prompt(self):
        return '\n>>> '

    @property
    def description(self):
        return ''

    @property
    def help(self):
        return ''

    def __repr__(self):
        return f'<Screen id={self.id!r} name={self.name!r}>'


class ScreenManager:
    _lastid = 0

    def __init__(self):
        self.history: List[Screen] = []
        self.running = True
        self.id = self.__class__._lastid
        self.screens: Dict[str, Screen] = {}
        self.__class__._lastid += 1

    def get_screen(self, id: str, default=None) -> Screen:
        return self.screens.get(id, default)

    @property
    def current(self) -> Screen:
        return self.history[-1]

    def goto(self, screen: Union[str, Screen]):
        id = screen
        if isinstance(screen, str):
            screen = self.get_screen(screen)

        if screen is None:
            raise ValueError(f'cannot find screen with id: {id}')

        if not self.history:
            self.history.append(screen)
        elif not self.current.can_leave(screen) or not screen.can_enter(self.current):
            return
        else:
            screen.on_enter()
            self.history.append(screen)
            self.current.on_leave()

    def back(self):
        if self.history[-2].can_enter(self.current):
            self.history.pop()

    def shutdown(self):
        self.running = False

    @property
    def can_go_back(self) -> bool:
        return len(self.history) > 1

    def run(self, initial: Union[str, Screen]):
        self.goto(initial)
        self.running = True

        while self.running:
            current = self.current
            print('\n\n\n\n', current.description, '\n', current.options, sep='')

            args = _parse_cmd(input(current.prompt))
            if not args:
                continue

            cmd, *args = args
            cmd = cmd.strip()

            if cmd.lower() in current.cmds:
                try:
                    current.cmds[cmd.lower()].execute(*args)
                except Exception as e:
                    print(f'"{current.id}" raised exception "{e}" of type {type(e)} when executing command {cmd}')
                    traceback.print_exc()
