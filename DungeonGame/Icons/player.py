from Config.config import WIDTH, ROWS
from Icons.MoveableIcon import MovableIcon


class Player(MovableIcon):
    def __init__(self, start_pos, lantern_fuel):
        super().__init__(start_pos, '@')
        self.fuel = lantern_fuel


