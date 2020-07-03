import sys
from random import choice, randint, choices
from typing import Optional

from arcade import *
from arcade import gui, key, color
from missile import Missile


class ArtGenGame(Window):
    def __init__(self, width: int = 800, height: int = 600, title: str = 'Arcade Window', fullscreen: bool = False, resizable: bool = False,
                 update_rate: Optional[float] = 1 / 60, antialiasing: bool = True):
        super().__init__(width, height, title, fullscreen, resizable, update_rate, antialiasing)
        self.missiles = []
        self.sprites = ShapeElementList()
        self.colors = [c for c in color.__dict__.values() if isinstance(c, tuple)]
        self._size_modifier = 1

    def gen_size(self):
        values = choices([1, 3, 5, 7, 9, 13, 20], [7, 6, 5, 4, 3, 2, 1], k=2)
        values[0] *= self._size_modifier
        values[1] *= self._size_modifier
        return values

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.sprites.append(create_ellipse_filled(x, y, *self.gen_size(), color=choice(self.colors)))

    def on_draw(self):
        start_render()
        self.sprites.draw()

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        self._size_modifier = max(self._size_modifier + 1 if scroll_y == 1 else -1, 1)


ArtGenGame()
run()
