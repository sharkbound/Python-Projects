from typing import Optional

from arcade import *
from arcade import key

from util.pos import *


class MainMenu(Window):
    def __init__(self, width: int = 800, height: int = 600, title: str = 'Arcade Window', fullscreen: bool = False, resizable: bool = False,
                 update_rate: Optional[float] = 1 / 60, antialiasing: bool = True):
        super().__init__(width, height, title, fullscreen, resizable, update_rate, antialiasing)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.ESCAPE:
            self.close()

    def on_draw(self):
        start_render()
        super().on_draw()

    def run(self):
        run()


MainMenu().run()
