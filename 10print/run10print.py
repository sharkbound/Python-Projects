# 
# reference: https://www.youtube.com/watch?v=jS824fCEG0o
# 


from random import random

from arcade import *
from arcade import color


class Game(Window):
    def __init__(self):
        super().__init__()
        self.thickness = 1
        self.length = self.width / 30
        self.lines = ShapeElementList()

    @property
    def center(self):
        return self.width / 2, self.height / 2

    def on_key_press(self, symbol: int, modifiers: int):
        self.lines = ShapeElementList()
        for x in range(0, int(self.width), int(self.length)):
            for y in range(0, int(self.height), int(self.length)):
                if random() < .5:
                    self.lines.append(create_line(x, y, x + self.length, y + self.length, color.RED))
                else:
                    self.lines.append(create_line(x, y + self.length, x + self.length, y, color.RED))

    def on_draw(self):
        cx, cy = self.center
        draw_rectangle_filled(cx, cy, self.width, self.height, color.BLACK)
        self.lines.draw()


Game()
run()
