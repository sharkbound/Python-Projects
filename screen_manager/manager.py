import traceback
from typing import List, Dict, Callable, Union, Any
from shlex import split


def _parse_cmd(text):
    try:
        v = split(text)
    except:
        v = text.split(' ')
    return v


class command:
    def __init__(self, name: str, desc: str = 'no description'):
        self.desc = desc
        self.name = name
        self.func: Callable[[List[str]], None] = lambda *_, **__: None

    def execute(self, *args):
        self.func(*args)

    def __call__(self, func):
        self.func = func
        return self


screens: Dict[str, 'Screen'] = {}


def get_screen(id: str, default=None) -> 'Screen':
    return screens.get(id, default)


class Screen:
    id: str
    name: str = 'MISSING NAME'

    cmds: Dict[str, command]

    def __init_subclass__(cls, **kwargs):
        if cls.__init__.__code__.co_argcount == 1:
            screens[cls.id] = cls()

    def __init__(self):
        self.cmds = {}
        self._find_cmds()

    def _find_cmds(self):
        for k, v in tuple(self.__class__.__dict__.items()):
            if isinstance(v, command):
                # we need to bind the function to the instance,
                # so we manually call __get__ on the function
                v.func = v.func.__get__(self)
                self.cmds[v.name.lower()] = v

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
    def __init__(self):
        self.history: List[Screen] = []
        self.running = True

    @property
    def current(self) -> Screen:
        return self.history[-1]

    @current.setter
    def current(self, screen: List[Screen]):
        self.history.append(screen)

    def back(self):
        self.history.pop()

    def shutdown(self):
        self.running = False

    @property
    def can_go_back(self) -> bool:
        return len(self.history) > 1

    def run(self, initial: Screen):
        self.current = initial
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
                    current.cmds[cmd].execute(*args)
                except Exception as e:
                    print(f'"{current.id}" raised exception "{e}" of type {type(e)} when executing command {cmd}')
                    traceback.print_exc()


mgr = ScreenManager()


class MainMenu(Screen):
    name = 'Billy'
    id = '1'

    @command('test')
    def cmd_test(self, *args):
        raise ValueError()


mgr.run(MainMenu())
