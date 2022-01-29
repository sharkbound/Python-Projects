import random
from collections import deque
from dataclasses import dataclass
from typing import NamedTuple

import arcade


def random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


class XY(NamedTuple):
    x: float
    y: float


@dataclass
class Triangle:
    p1: XY
    p2: XY
    color: tuple
    alpha: int

    @property
    def color_with_alpha(self):
        return self.color + (self.alpha,)


class MainView(arcade.View):
    def __init__(self):
        super().__init__()
        self.points = deque(maxlen=300)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if len(self.points) < 2:
            self.points.append(Triangle(XY(x, y), XY(x, y), random_color(), 255))
            return

        if abs(self.points[-1].p2.x - x) + abs(self.points[-1].p2.y - y) >= random.randint(10, 200):
            self.points.append(Triangle(self.points[-1].p2, XY(x, y), random_color(), random.randrange(255)))

        for point_to_remove in [p for p in self.points if p.alpha <= 0]:
            self.points.remove(point_to_remove)

    def update(self, delta_time: float):
        self.window.set_caption(str(1 / delta_time))
        for point in self.points:
            point.alpha = max(0, point.alpha - 1)

    def on_draw(self):
        arcade.start_render()
        for tri in self.points:
            arcade.draw_triangle_filled(tri.p1.x, tri.p1.y,
                                        tri.p2.x, tri.p2.y,
                                        self.window._mouse_x, self.window._mouse_y,
                                        tri.color_with_alpha)


window = arcade.Window()
window.show_view(MainView())
arcade.run()
