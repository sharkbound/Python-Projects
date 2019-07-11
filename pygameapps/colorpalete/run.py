import re
from typing import Union, Tuple, Optional

from pygame_util import *

setup()


class Colors:
    def __init__(self, *colors: Union[Tuple[int, int, int, ...], Color]):
        self.colors: List[Color] = list(map(self._ensure_color, colors))

    def add(self, color):
        self.colors.append(self._ensure_color(color))

    def add_all(self, *colors):
        self.colors.extend(map(self._ensure_color, colors))

    def _is_hex(self, value):
        return isinstance(value, str) and '#' in value and re.match('^#[a-zA-Za-fA-F]{6}|[a-zA-Za-fA-F]{8}$', value)

    def _ensure_color(self, value) -> Color:
        if isinstance(value, Color):
            return value
        if isinstance(value, (tuple, list)):
            self._check_size(value)
            return Color(*value)
        if self._is_hex(value):
            return Color(value)

        try:
            return Color(value)
        except:
            pass

        try:
            return Color(*value)
        except:
            pass

        raise ValueError(
            f'bad color value "{value}", must be a color name, hex (6 or 8 length), or a list (3 or 4 length)')

    def _check_size(self, value):
        if len(value) not in (3, 4):
            raise ValueError(
                f'length of list/tuple must be 3 (R, G, B) or 4 (R, G, B, A), but got length {len(value)}')


while running():
    for e in get_events():
        check_quit(e)
