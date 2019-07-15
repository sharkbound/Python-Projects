import pygame
from pygame_util.data import Point
from pygame_util import settings
from pygame_util.helpers import *


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def pos(self):
        return self.x, self.y

    @property
    def vector(self):
        return Vector2(self.x, self.y)

    def move(self, x=None, y=None, relx=None, rely=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if relx is not None:
            self.x += relx
        if rely is not None:
            self.y += rely

    def keep_in_bounds(self, size):
        self.x %= size[0]
        self.y %= size[1]

    def __iter__(self):
        yield self.x
        yield self.y

    def __str__(self):
        return f'[{self.x}, {self.y}]'
