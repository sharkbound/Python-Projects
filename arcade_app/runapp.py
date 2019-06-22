from arcade import *


class MainWindow(Window):
    def __init__(self):
        super().__init__()

        self.sprites = SpriteList()
        self.circle_draw_pos = 0, 0
        self.circle_color = 255, 255, 0

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, buttons: int, modifiers: int):
        self.circle_draw_pos = x, y

    def on_draw(self):
        start_render()

        x, y = self.circle_draw_pos
        draw_circle_outline(x, y, 10, self.circle_color)


MainWindow()
run()
