from typing import Union
from .helpers import draw_rect, Rect, Color, render_rect


class ProgressBar:
    def __init__(self, rect: Rect, init_value=0.0, max_value=100.0, color: Union[Color, tuple] = (255, 0, 0)):
        self.rect: Rect = rect
        self.color: Color = Color(*color) if not isinstance(color, Color) else color
        self.max_value: float = max_value
        self._value: float = init_value

    @property
    def progress(self):
        return self._value / self.max_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        print(f'now {self._value} next {self._value + v}')
        self._value = max(0.0, min(self._value + v, self.max_value))

    def draw(self, color=None):
        color = self.color if color is None else color
        render_rect(color, self.rect, 1)
        draw_rect(color, self.rect.x, self.rect.y, self.rect.w * self.progress, self.rect.h)
