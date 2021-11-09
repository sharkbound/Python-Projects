from enum import Enum, auto
from random import randrange, choice, random, shuffle

from arcade import *
from arcade import color
from inspect import getmembers

colors = [c for c in getmembers(color) if type(c) is tuple]
shuffle(colors)


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

    def random(self) -> 'Direction':
        return choice(ALL_DIRECTIONS)


ALL_DIRECTIONS = tuple(Direction)


class Painter:
    def __init__(self):
        self.x, self.y = randrange(get_window().width), randrange(get_window().height)
        self.color = colors.pop()

    def __repr__(self):
        return f'<Painter x={self.x} y={self.y}>'


class Game(Window):
    def __init__(self):
        super().__init__()
        self.painters = Painter()


win = Game()
run()
