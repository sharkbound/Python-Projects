import pygame as pg

from .data import Point
from pygame_util.helpers import *


class Button:
    def __init__(self, pos, width, height, color=None):
        self.color = to_color(color)
        self.height = height
        self.width = width
        self.pos = Point(pos)

    @property
    def hovered(self):
        x1, x2, y1, y2 = self.pos.x, self.pos.x + self.width, self.pos.y, self.pos.y + self.height
        mx, my = pg.mouse.get_pos()
        return min(x1, x2) <= mx <= max(x1, x2) and min(y1, y2) <= my <= max(y1, y2)

    def pressed(self, event=None):
        if event is not None:
            return self.hovered and event.type == pg.MOUSEBUTTONDOWN and event.button == 1
        return self.hovered and pg.mouse.get_pressed()[0]

    def draw(self, color=None, width=0):
        draw_rect(to_color(color or self.color), *self.pos, self.width, self.height, width)

# def button(text: str, rect: Rect, normal_color: Union[Color, Tuple[int, int, int]],
#            hovered_color: Union[Color, Tuple[int, int, int]], onclick=None, onhover=None):
#     draw_rect()
