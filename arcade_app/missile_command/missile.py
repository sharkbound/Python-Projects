from typing import TYPE_CHECKING

from arcade import draw_line, color, draw_circle_filled

from vecf import VecF

if TYPE_CHECKING:
    from run_missile_command import MissileCommandGame


class Missile:
    _id = 0

    def __init__(self, origin: VecF, target: VecF, max_size: int = 20, color: tuple = color.RED):
        Missile._id += 1

        self.original_color = color
        self.color = color
        self.max_size = max_size
        self.origin = origin
        self.target = target
        self.radius = 0
        self.alive = True
        self.id = Missile._id

    def check_collision(self, point: VecF):
        return self.target.distance(point) <= self.radius

    def update(self):
        if self.radius == -1: return

        self.radius += 1
        if self.radius > self.max_size:
            self.radius = -1
            self.alive = False

    def on_draw(self):
        draw_line(*self.origin, *self.target, color=self.color)
        draw_circle_filled(*self.target, self.radius, color=self.color)
