from typing import TYPE_CHECKING

from arcade import draw_line, color

from vecf import VecF

if TYPE_CHECKING:
    from run_missile_command import MissileCommandGame


class Missile:
    def __init__(self, origin: VecF, target: VecF):
        self.origin = origin
        self.target = target

    def update(self):
        pass

    def on_draw(self):
        draw_line(*self.origin, *self.target, color=color.GREEN)
