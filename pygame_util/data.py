from typing import Iterable
from decimal import Decimal
from pygame.math import Vector2
import math


class Point(Vector2):
    __zero = None

    def __init__(self, *args):
        super().__init__(*args)

        # if len(args) == 2:
        #     x, y = args
        # elif len(args) == 1:
        #     x, y = args[0]
        # else:
        #     raise ValueError('arguments must be a iterable of length 2 with x and y value, or be x and y alone')
        # self.x, self.y = x, y

    def fill(self, digit=0):
        self.x, self.y = digit, digit

    def dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def to_vector(self):
        return Vector2(self.x, self.y)

    def copy(self):
        return Point(self.x, self.y)

    @staticmethod
    def lerp(start, end, percent):
        return Point(Vector2.lerp(start, end, percent))

    @staticmethod
    def slerp(start, end, percent):
        return Point(Vector2.slerp(start, end, percent))

    @classmethod
    def zero(cls):
        if cls.__zero is None:
            cls.__zero = cls(0, 0)
        return cls.__zero

    def __getitem__(self, item):
        if item in ('x', 0):
            return self.x
        if item in ('y', 1):
            return self.y

    def __setitem__(self, key, value):
        if not isinstance(value, (int, float, Decimal)):
            raise ValueError('value must be int, float, or Decimal')

        if key in ('x', 0):
            self.x = value
        elif key in ('y', 1):
            self.y = value

    def __repr__(self):
        return f'Point({round(self.x)}, {round(self.y)})'

    def __str__(self):
        return f'[{self.x}, {self.y}]'

    def __iter__(self):
        yield math.floor(self.x) if str(self.x)[-2:] == '.0' else self.x
        yield math.floor(self.y) if str(self.y)[-2:] == '.0' else self.y

    def __eq__(self, other):
        return self[0] is other[0] and self[1] is other[1]

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self[0] > other[0] and self[1] > other[1]

    def __lt__(self, other):
        return not self > other

    def __mul__(self, other):
        if isinstance(other, (int, float, Decimal)):
            self.x *= other
            self.y *= other
        else:
            self.x *= other[0]
            self.y *= other[1]
        return self

    __rmul__ = __mul__
    __imul__ = __mul__

    def __add__(self, other):
        if isinstance(other, (int, float, Decimal)):
            self.x += other
            self.y += other
        else:
            self.x += other[0]
            self.y += other[1]
        return self

    __radd__ = __add__
    __iadd__ = __add__

    def __sub__(self, other):
        if isinstance(other, (int, float, Decimal)):
            self.x -= other
            self.y -= other
        else:
            self.x -= other[0]
            self.y -= other[1]
        return self

    __rsub__ = __sub__
    __isub__ = __sub__

    def __truediv__(self, other):
        if isinstance(other, (int, float, Decimal)):
            self.x /= other
            self.y /= other
        else:
            self.x /= other[0]
            self.y /= other[1]
        return self

    __rtruediv__ = __truediv__
    __itruediv__ = __truediv__

    def __floordiv__(self, other):
        if isinstance(other, (int, float, Decimal)):
            self.x //= other
            self.y //= other
        else:
            self.x //= other[0]
            self.y //= other[1]
        return self

    __rfloordiv__ = __floordiv__
    __ifloordiv__ = __floordiv__

    def __mod__(self, other):
        if isinstance(other, (int, float, Decimal)):
            self.x %= other
            self.y %= other
        else:
            self.x %= other[0]
            self.y %= other[1]
        return self

    __rmod__ = __mod__
    __imod__ = __mod__
