import random
from collections import deque
from dataclasses import dataclass

import arcade


def random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


@dataclass
class XY:
    __slots__ = ('x', 'y')
    x: float
    y: float


@dataclass
class Point:
    x: float
    y: float
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
        if not self.points:
            self.points.append(Point(x, y, random_color(), 255))
            return

        dist = 15
        if abs(self.points[-1].x - x) + abs(self.points[-1].y - y) >= dist:
            self.points.append(Point(x, y, random_color(), 255))

        for point_to_remove in [p for p in self.points if p.alpha <= 0]:
            self.points.remove(point_to_remove)

    def update(self, delta_time: float):
        self.window.set_caption(str(1 / delta_time))
        for point in self.points:
            point.alpha -= 2

    def on_draw(self):
        arcade.start_render()
        for point in self.points:
            arcade.draw_line(point.x, point.y, self.window._mouse_x, self.window._mouse_y, point.color_with_alpha)


window = arcade.Window()
window.show_view(MainView())
arcade.run()
