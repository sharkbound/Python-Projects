import sys
from random import choice, randint, choices, randrange
from typing import Optional, List, Any

from arcade import *
from arcade import gui, key, color
from missile import Missile
from vecf import VecF

ALL_COLORS = [c for c in color.__dict__.values() if isinstance(c, tuple)]


class MissileCommandGame(Window):
    missiles: List[Missile]

    def __init__(self, width: int = 800, height: int = 600, title: str = 'Arcade Window', fullscreen: bool = False, resizable: bool = False,
                 update_rate: Optional[float] = 1 / 60, antialiasing: bool = True):
        super().__init__(width, height, title, fullscreen, resizable, update_rate, antialiasing)
        self.missiles = []

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        super().on_mouse_press(x, y, button, modifiers)
        if button == MOUSE_BUTTON_LEFT:
            self.missiles.append(self.create_missile_from_mouse_pos())

    def create_missile_from_mouse_pos(self):
        return Missile(VecF(randrange(self.width), 0), VecF(self._mouse_x, self._mouse_y), randint(30, 200), color=choice(ALL_COLORS))

    def on_update(self, delta_time: float):
        super().on_update(delta_time)
        for missile in self.missiles:
            missile.update()

        for missile in [m for m in self.missiles if not m.alive]:
            self.missiles.remove(missile)

    def on_draw(self):
        start_render()

        for missile in self.missiles:
            missile.on_draw()


MissileCommandGame()
run()
