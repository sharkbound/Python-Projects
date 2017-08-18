from Config.config import ROWS, WIDTH


class MovableIcon:
    def __init__(self, start_pos, symbol):
        self.symbol = symbol
        self.pos = start_pos
        self.last_pos = self.pos

    @property
    def X(self):
        return self.pos[0]

    @X.setter
    def X(self, new_x):
        self.set_pos(new_x, self.Y)

    @property
    def Y(self):
        return self.pos[1]

    @Y.setter
    def Y(self, new_y):
        self.set_pos(self.X, new_y)

    def move_rel(self, x=0, y=0, free_spaces=()):
        self.set_pos(self.X + x, self.Y + y, free_spaces)

    def set_pos(self, x, y, free_spaces=()):
        if x >= WIDTH or x < 0:
            x = WIDTH-1 if x >= WIDTH else 0
        if y >= ROWS or y < 0:
            y = WIDTH-1 if y >= ROWS else 0

        if (x, y) != self.pos:
            self.last_pos = self.pos
            self.pos = (x, y)

    def move_to_last_pos(self):
        self.set_pos(self.last_pos[0], self.last_pos[1])

    @property
    def move_diff(self):
        return (self.X - self.last_pos[0], self.Y - self.last_pos[0])

    def check_collision(self, other):
        return self.pos == other.pos

    def __call__(self, *args, **kwargs):
        pass

    def __repr__(self):
        return f'LAST: {self.last_pos}, CURRENT: {self.pos} CHANGE: {self.move_diff}'
