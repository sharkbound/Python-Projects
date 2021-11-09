from dataclasses import dataclass
from typing import Tuple, List

from arcade import Window, Vector


class VecF:
    __slots__ = 'x', 'y'

    def __init__(self, x: float, y: float):
        self.y = y
        self.x = x

    def as_tuple(self):
        return self.x, self.y

    def distance(self, other: ('VecF', List, Tuple)):
        return abs(self.x - other[0]) + abs(self.y - other[1])

    def __iter__(self):
        return iter(self.as_tuple())

    def __getitem__(self, item):
        if item in ('x', 0):
            return self.x
        if item in ('y', 1):
            return self.y

    def __add__(self, other) -> 'VecF':
        if isinstance(other, (VecF, List, Tuple)):
            return self.__class__(self.x + other[0], self.y + other[1])
        raise ValueError(f'got type `{type(other)}` in __add__ for VecF, expected types: {(VecF, List, Tuple)}')

    def __sub__(self, other) -> 'VecF':
        if isinstance(other, (VecF, List, Tuple)):
            return self.__class__(self.x - other[0], self.y - other[1])
        raise ValueError(f'got type `{type(other)}` in __sub__ for VecF, expected types: {(VecF, List, Tuple)}')

    def __mul__(self, other) -> 'VecF':
        if isinstance(other, (VecF, List, Tuple)):
            return self.__class__(self.x * other[0], self.y * other[1])
        raise ValueError(f'got type `{type(other)}` in __mul__ for VecF, expected types: {(VecF, List, Tuple)}')

    def __truediv__(self, other) -> 'VecF':
        if isinstance(other, (VecF, List, Tuple)):
            return self.__class__(self.x / other[0], self.y / other[1])
        raise ValueError(f'got type `{type(other)}` in __truediv__ for VecF, expected types: {(VecF, List, Tuple)}')

    def __mod__(self, other) -> 'VecF':
        if isinstance(other, (VecF, List, Tuple)):
            return self.__class__(self.x % other[0], self.y % other[1])
        raise ValueError(f'got type `{type(other)}` in __mod__ for VecF, expected types: {(VecF, List, Tuple)}')


def center(window: Window) -> VecF:
    return VecF(window.width / 2, window.height / 2)


def top_left(window: Window) -> VecF:
    return VecF(0, window.height)


def top_right(window: Window) -> VecF:
    return VecF(window.width, window.height)


def bottom_left(window: Window) -> VecF:
    return VecF(0, 0)


def bottom_right(window: Window) -> VecF:
    return VecF(window.width, 0)
