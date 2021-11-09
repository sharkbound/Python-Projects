from pygame import Vector2
from numpy import clip


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_vector(cls, value: Vector2) -> 'Position':
        return cls(x=value.x, y=value.y)

    @classmethod
    def from_tuple(cls, value) -> 'Position':
        return cls(x=value[0], y=value[1])

    @property
    def pos(self):
        return int(self.x), int(self.y)

    @property
    def vector(self):
        return Vector2(int(self.x), int(self.y))

    def move(self, x=None, y=None, relx=None, rely=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if relx is not None:
            self.x += relx
        if rely is not None:
            self.y += rely

    def keep_in_bounds(self, size, loop=True):
        if loop:
            self.x %= size[0]
            self.y %= size[1]
        else:
            self.x = clip(self.x, 0, size[0] - 1)
            self.y = clip(self.y, 0, size[1] - 1)

    def __getitem__(self, item):
        if item in (0, 'x'):
            return self.x
        if item in (1, 'y'):
            return self.y

    def __iter__(self):
        yield self.x
        yield self.y

    def __str__(self):
        return f'[{self.x}, {self.y}]'


def clamp(v, min_, max_):
    return max(min_, min(v, max_))
