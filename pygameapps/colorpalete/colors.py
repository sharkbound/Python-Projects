import re
from itertools import chain
from typing import Tuple, List, Iterable, Union, Dict, Any
from pygame import Color

ColorType = Union[
    str,
    Color,
    Tuple[int, int, int],
    Tuple[int, int, int, int],
    List[int],
]


class Colors:
    def __init__(self, *colors: ColorType, **named: ColorType):
        self.colors: List[Color] = list(map(self._ensure_color, colors))
        self.named: Dict[Any, Color] = {name: self._ensure_color(value) for name, value in named.items()}

    def append(self, color):
        self.colors.append(self._ensure_color(color))

    def append_all(self, *colors: ColorType):
        self.colors.extend(map(self._ensure_color, colors))

    def add_named(self, key, value: ColorType):
        self.named[key] = self._ensure_color(value)

    def add_named_all(self, *pairs: Tuple[Any, ColorType], **named: ColorType):
        for key, value in chain(pairs, named.items()):
            self.add_named(key, value)

    def extend(self, iterable: Iterable[ColorType]):
        for item in iterable:
            if isinstance(item, Iterable):
                self.extend(item)
            else:
                self.colors.append(self._ensure_color(item))

    def _is_hex(self, value):
        return isinstance(value, str) and '#' in value and re.match('^#(?P<hex>[1-9a-fA-F]{8}|[1-9a-fA-F]{6})$', value)

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
            f'bad color value "{value}", must be a color name, hex (6 or 8 length), or a list/tuple (3 or 4 length)')

    def _check_size(self, value):
        if len(value) not in (3, 4):
            raise ValueError(
                f'length of list/tuple must be 3 (R, G, B) or 4 (R, G, B, A), but got length {len(value)}')

    def __getitem__(self, item) -> Color:
        if isinstance(item, int):
            return self.colors[item]
        return self.named[item]

    def __setitem__(self, key, value: ColorType):
        if isinstance(key, int):
            self.colors.insert(key, value)
        self.named[key] = self._ensure_color(value)

    def __getattr__(self, item):
        return self.named[item]

    def __iter__(self):
        yield from self.colors

    def __len__(self):
        return len(self.colors)

    def __str__(self):
        named_colors = '\n\t'.join(f'{k}={v}' for k, v in self.named.items()) if self.named else ''
        unnamed_colors = '\n\t\t'.join(f'{i}: {v}' for i, v in enumerate(map(repr, self.colors)))
        return f'<{self.__class__.__name__}\n\t{named_colors}\n\tunamed:\n\t\t{unnamed_colors}\n{self.__class__.__name__}>'

    def __repr__(self):
        return f'<{self.__class__.__name__} len={len(self)}>'


x = Colors(red=(1, 1, 1))
x.append('#ff00ff00')
x.append_all('green', 'blue', (1, 200, 255, 100))
x.add_named_all(('red', (1, 1, 100, 1)), blue='#badc0d')
print(x)
