from random import choice, randint, randrange
from random import choice, randint, randrange
from typing import Optional, List

from arcade import *
from arcade import color
import arcade

from missile import Missile
from vecf import VecF

ALL_COLORS = [c for c in color.__dict__.values() if isinstance(c, tuple)]


class MissileCommandGame(Window):

    def __init__(self, width: int = 800, height: int = 600, title: str = 'Arcade Window', fullscreen: bool = False, resizable: bool = False,
                 antialiasing: bool = True):
        super().__init__(width, height, title, fullscreen, resizable, 1 / 60, antialiasing)
        self.missiles: List[Missile] = []
        self.delta_time = 1

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == MOUSE_BUTTON_LEFT:
            self.missiles.append(self.create_missile_from_mouse_pos())

    def create_missile_from_mouse_pos(self):
        return Missile(VecF(randrange(self.width), 0), VecF(self._mouse_x, self._mouse_y), randint(30, 200), color=choice(ALL_COLORS))

    def on_update(self, delta_time: float):
        for missile in self.missiles:
            missile.update(delta_time)

        for missile in [m for m in self.missiles if not m.alive]:
            self.missiles.remove(missile)

        self.delta_time = delta_time

    def on_draw(self):
        start_render()

        if self.missiles:
            for missile in self.missiles:
                missile.draw()

        draw_text(f'FPS: {int(1 / self.delta_time)}', 10, 10, color.GOLD)


MissileCommandGame()
run()
