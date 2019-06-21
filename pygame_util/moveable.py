import pygame
from .data import Point
from pygame_util import settings
from pygame_util.helpers import *


class Moveable:
    def __init__(self, pos=(), color=()):
        self._pos = Point(pos or random_pos())
        self.last = Point(self.x, self.y)
        self.color = color or random_color()

    @property
    def x(self):
        return self._pos.x

    @property
    def y(self):
        return self._pos.y

    @x.setter
    def x(self, value):
        self.set_pos(new_x=value)

    @y.setter
    def y(self, value):
        self.set_pos(new_y=value)

    @property
    def pos(self):
        return Point(*self._pos)

    @pos.setter
    def pos(self, value):
        self._pos = Point(value)

    def randomize_color(self):
        self.color = random_color()

    def keep_in_bounds(self):
        self._pos.x %= settings.size[0]
        self._pos.y %= settings.size[1]

    def set_pos(self, new_x=None, new_y=None, offx=None, offy=None, check=True):
        if self.last != self._pos:
            self.last.x, self.last.y = self.x, self.y

        if not new_x: new_x = self.x
        if not new_y: new_y = self.y

        if offx or offy:
            new_x = self.x + (offx or 0)
            new_y = self.y + (offy or 0)

        self._pos.x, self._pos.y = new_x, new_y
        if check:
            self.keep_in_bounds()

    def set_pos_no_check(self, new_x=None, new_y=None, offx=None, offy=None):
        self.set_pos(new_x, new_y, offx, offy, False)

    def move(self, x=None, y=None, check=True):
        self.set_pos(offx=x, offy=y, check=check)

    def distance(self, other):
        return self._pos.distance_to(other)

    def draw_rect(self, len_x=1, len_y=1, width=0, color=None):
        draw_rect(color or self.color, *self._pos, len_x, len_y, width)

    def draw_line(self, dest, width=1, color=None):
        draw_line(color or self.color, self._pos, dest, width)

    def draw_circle(self, radius, width=0, color=None):
        draw_circle(color or self.color, [int(x) for x in self._pos], int(radius), int(width))

    def draw_poly(self, pointlist, width=0, color=None, relative=False):
        if relative:
            pointlist = [(self[0] + x[0], self[1] + x[1]) for x in pointlist]
        draw_poly(color or self.color, [self._pos] + pointlist, width)

    def __getitem__(self, item):
        if item == 'x' or item == 0:
            return self._pos.x
        elif item == 'y' or item == 1:
            return self._pos.y
        elif item == 'color':
            return self.color
        elif item == 'pos':
            return self._pos

    def __setitem__(self, key, value):
        if key == 'x' or key == 0:
            self._pos.x = value
        elif key == 'y' or key == 1:
            self._pos.y = value
        elif key == 'pos':
            if len(value) == 3 and value[2]:
                self.set_pos(offx=value[0], offy=value[1])
            else:
                self.set_pos(new_x=value[0], new_y=value[1])
        elif key == 'color':
            if isinstance(value, pygame.Color):
                self.color = value
            elif isinstance(value, str):
                self.color = pygame.Color(value)
            else:
                self.color = pygame.Color(*value)

    def __iter__(self):
        yield from self._pos

    def __call__(self):
        self.keep_in_bounds()

    def __str__(self):
        return f'[{self.x}, {self.y}]'
