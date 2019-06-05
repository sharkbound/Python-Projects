from typing import List, Dict, Callable, Union, Any


class command:
    def __init__(self, name: str):
        self.name = name
        self.func = lambda *_, **__: None

    def __call__(self, func):
        self.func = func
        return self


screens: Dict[str, 'Screen'] = {}


def get_screen(id: str, default=None) -> 'Screen':
    return screens.get(id, default)


class Screen:
    id: str
    name: str = 'MISSING NAME'

    cmds: Dict[str, Callable[[List[str]], None]]

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
                f = v.func.__get__(self)
                self.cmds[v.name] = f
                self.__dict__[k] = f

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
        return

    @property
    def prompt(self):
        return

    @property
    def description(self):
        return

    @property
    def help(self):
        return

    def __repr__(self):
        return f'<Screen id={self.id!r} name={self.name!r}>'


class ScreenManager:
    def __init__(self):
        self.history: List[Screen] = []

    @property
    def current(self) -> Screen:
        return self.history[-1]

    @current.setter
    def current(self, screen: List[Screen]):
        self.history.append(screen)

    def back(self):
        self.history.pop()

    @property
    def can_go_back(self) -> bool:
        return len(self.history) > 1

    def run(self, initial: Screen):
        pass


mgr = ScreenManager()
