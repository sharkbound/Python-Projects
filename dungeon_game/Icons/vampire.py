from random import randint

from Config.config import ROWS, WIDTH
from Icons.MoveableIcon import MovableIcon


class Vampire(MovableIcon):
    def __init__(self, start_pos):
        super().__init__(start_pos, 'V')

    def __call__(self, free_spaces=()):
        x = randint(-1, 1)
        if x:
            self.move_rel(x=x)
        else:
            self.move_rel(y=randint(-1, 1))

    def set_pos(self, x, y, free_spaces=()):
        # x, y = x % WIDTH, y % ROWS

        if x >= WIDTH or x < 0:
            x = WIDTH-1 if x >= WIDTH else 0
        if y >= ROWS or y < 0:
            y = WIDTH-1 if y >= ROWS else 0

        if free_spaces and (x, y) not in free_spaces:
            # print('[DEBUG MOVEABLEICON] not in free spaces for', type(self).__name__, 'free spaces:', free_spaces, 'x, y demanded', (x, y))
            x, y = self.X, self.Y

        if (x, y) != self.pos:
            self.last_pos = self.pos
            self.pos = (x, y)