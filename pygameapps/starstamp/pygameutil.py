import copy
from decimal import Decimal
from math import cos, radians, sin
from random import *
from typing import Dict, Any
from typing import Tuple

import pygame
from pygame import *
from pygame.font import SysFont, Font as PyGameFont
from pygame.math import Vector2

try:
    from .data import Point
except ImportError:
    Point = Vector2

size: Tuple[int, int] = None
surface: Surface = None


# ------------
#    SETUP
# ------------


def setup(window_size=(600, 600), flags=0, depth=0) -> Surface:
    global size, surface

    init()
    size = window_size
    surface = display.set_mode(window_size, flags, depth)

    return surface


def set_window_title(title, icon=None):
    pygame.display.set_caption(title, icon)


def get_clock():
    return pygame.time.Clock()


# ----------
#   EVENTS
# ----------

def get_events():
    return event.get()


def get_key_down(e):
    if e.type == KEYDOWN:
        return e.key


def get_key_up(e):
    if e.type == KEYUP:
        return e.key


def get_mouse_down(e):
    if e.type == MOUSEBUTTONDOWN:
        return e.button


def get_mouse_up(e):
    if e.type == MOUSEBUTTONUP:
        return e.button


def quit_pygame():
    pygame.quit()
    exit()


def check_quit(event, on_quit=None, quit_keys=(K_ESCAPE,)):
    if event.type == QUIT or event.type == KEYDOWN and event.key in quit_keys:
        if on_quit:
            on_quit()
        quit_pygame()


# ------------
#   KEYBOARD
# ------------
def get_pressed_keys():
    return key.get_pressed()


def mod_held(mod):
    return bool(get_mods() & mod)


def key_held(key):
    return bool(get_pressed_keys()[key])


def key_down(e, key):
    return e.type == KEYDOWN and e.key == key


def key_up(e, key):
    return e.type == KEYUP and e.key == key


def handle_key_press(k, actions):
    actions.get(k, lambda: None)()


def handle_key_down(e, actions):
    if e.type == KEYDOWN:
        handle_key_press(e.key, actions)


def handle_key_up(e, actions):
    if e.type == KEYUP:
        handle_key_press(e.key, actions)


def do_if_pressed(key, func):
    if key_held(key):
        func()


# ------------
#    MOUSE
# ------------
def get_mouse_pos() -> Tuple[int, int]:
    return mouse.get_pos()


def get_mouse_pos_vect() -> Vector2:
    return Vector2(get_mouse_pos())


def set_mouse_pos(x, y):
    mouse.set_pos(x, y)
    return (x, y)


def set_mouse_visible(bool):
    mouse.set_visible(bool)


def mouse_button_held(btn_code):
    return bool(mouse.get_pressed()[btn_code])


# ------------
#   SCREEN
# ------------
def get_center(int_div=False, axis=None):
    center = (size[0] // 2 if int_div else size[0] / 2,
              size[1] // 2 if int_div else size[1] / 2)
    if axis:
        return center[axis]
    return center


def get_width():
    return size[0]


def get_height():
    return size[1]


def fill_screen(color='black', rect=None):
    surface.fill(to_color(color), rect)


def random_pos(padding=1, max_x: int = None, max_y: int = None) -> Tuple[int, int]:
    if max_x is None:
        max_x = size[0]
    if max_y is None:
        max_y = size[1]

    x, y = randint(0, max_x), randint(0, max_y)
    if x >= max_x / 2:
        x -= padding
    else:
        x += padding
    if y >= max_y / 2:
        y -= padding
    else:
        y += padding
    return x, y


def random_pos_vect(padding=1) -> Vector2:
    return Vector2(random_pos(padding))


def random_color(random_alpha=True):
    return Color(randrange(256), randrange(256), randrange(256), randint(1, 255) if random_alpha else 255)


def update():
    display.update()


def blit(item, dest, area=None, special_flags=0):
    surface.blit(item, dest, area, special_flags)


def get_surface():
    return surface


def keep_in_bounds_rect(rect: Rect, bounds=None):
    if bounds is None:
        bounds = size

    if rect.centerx > bounds[0]:
        rect.centerx = bounds[0]
    elif rect.centerx < 0:
        rect.centerx = 0

    if rect.centery > bounds[1]:
        rect.centery = bounds[1]
    elif rect.centery < 0:
        rect.centery = 0

    return rect


def keep_in_bounds_loop_rect(rect: Rect, bounds=None):
    if bounds is None:
        bounds = size

    if rect.centerx > bounds[0]:
        rect.centerx = 0
    elif rect.centerx < 0:
        rect.centerx = bounds[0]

    if rect.centery > bounds[1]:
        rect.centery = 0
    elif rect.centery < 0:
        rect.centery = bounds[1]

    return rect


def keep_in_bounds(pos, bounds=None):
    if bounds is None:
        bounds = size

    if pos[0] > bounds[0]:
        pos[0] = bounds[0]
    elif pos[0] < 0:
        pos[0] = 0

    if pos[1] > bounds[1]:
        pos[1] = bounds[1]
    elif pos[1] < 0:
        pos[1] = 0

    return pos


def keep_in_bounds_loop(pos, bounds=None):
    if bounds is None:
        bounds = size

    if pos[0] > bounds[0]:
        pos[0] = 0
    elif pos[0] < 0:
        pos[0] = bounds[0]

    if pos[1] > bounds[1]:
        pos[1] = 0
    elif pos[1] < 0:
        pos[1] = bounds[1]

    return pos


def check_in_bounds(pos):
    return 0 <= pos[0] <= get_width() and 0 <= pos[1] <= get_height()


# --------
#   TEXT
# --------
def create_font(name, size, bold=False, italic=False):
    return font.SysFont(name, size, bold, italic)


# ---------
#  DRAWING
# ---------

def render_rect(color, rect: Rect, width=0):
    draw.rect(surface, color, rect, width)


def draw_rect(color, x, y, lenx, leny, width=0):
    draw.rect(surface, to_color(color), (x, y, lenx, leny), width)


def draw_square(color, x, y, size, width=0):
    draw.rect(surface, to_color(color), (x, y, size, size), width)


def draw_circle(color, pos, radius, width=0):
    draw.circle(surface, to_color(color), tuple(map(int, pos)), radius, width)


def draw_line(color, start_pos, end_pos, width=1):
    draw.line(surface, to_color(color), start_pos, end_pos, width)


def draw_lines(color, closed, pointlist, width=1):
    draw.lines(surface, to_color(color), closed, pointlist, width)


def draw_connecting_lines(color, pointlist, width=1):
    last = pointlist[0]
    for p in pointlist[1:]:
        draw_line(color, last, p, width)
        last = p


def draw_poly(color, pointlist, width=0):
    draw.polygon(surface, to_color(color), pointlist, width)


def draw_aaline(color, startpos, endpos, blend=1):
    draw.aaline(surface, to_color(color), startpos, endpos, blend)


# -------
#  COLOR
# -------
def to_color(*args):
    if len(args) == 1:
        if isinstance(args[0], Color):
            return args[0]

        elif isinstance(args[0], str):
            return Color(args[0])

        elif isinstance(args[0], (tuple, list)):
            return Color(*args[0])

        raise TypeError(f'invalid type: {type(args[0])}')

    elif len(args) >= 3:
        return Color(*args)

    raise ValueError(f'invalid length for *args at to_color(): {len(args)}, expected: 1 or 3+')


# ------
#  MATH
# ------

def clamp(x, minv=0, maxv=1):
    return max(minv, min(x, maxv))


def dcos(x, dist, angle):
    """ same as cos(), but does x + dist * cos(angle) """
    return x + dist * cos(angle)


def dsin(x, dist, angle):
    """ same as sin(), but does x + dist * sin(angle) """
    return x + dist * sin(angle)


def rdcos(x, dist, angle):
    """ runs dcos(), but converts angle to radians """
    return x + dist * cos(radians(angle))


def rdsin(x, dist, angle):
    """ runs dsin(), but converts angle to radians """
    return x + dist * sin(radians(angle))


def rcos(x):
    """ converts x to radians then passes the radians to cos() """
    return cos(radians(x))


def rsin(x):
    """ converts x to radians then passes the radians to sin() """
    return sin(radians(x))


def random_force(min_force, max_force):
    return (uniform(min_force, max_force), uniform(min_force, max_force))


# ------
#  MISC
# ------

def square(center, size):
    return Rect(center[0] - size, center[1] - size, size * 2, size * 2)


def get_mods():
    return key.get_mods()


def deepcopy(obj):
    return copy.deepcopy(obj)


def get_ticks():
    return pygame.time.get_ticks()


def wait(ms):
    pygame.time.wait(ms)


def is_coord(obj):
    if isinstance(obj, (tuple, list)) and len(obj) == 2:
        return True
    return isinstance(obj, (Vector2, Point))


def snap_to_grid(pos, grid_size):
    if isinstance(grid_size, (int, float, Decimal)):
        x_width = y_width = grid_size
    else:
        x_width, y_width = grid_size

    if isinstance(pos, tuple):
        return round(pos[0] / x_width) * x_width, round(pos[1] / y_width) * y_width

    pos[0] = (pos[0] // x_width) * x_width
    pos[1] = (pos[1] // y_width) * y_width
    return pos


def find_center(size):
    return size[0] // 2, size[1] // 2


def dist(start, end, index=None, to_abs=True):
    if is_coord(start) and is_coord(end):
        if index is not None:
            return abs(start[index] - end[index])
        return Vector2(start).distance_to(end)

    # obj is not of type tuple, list, Point, or Vector2, assume it is a number
    return abs(start - end) if to_abs else start - end


# --------
# CLASSES
# --------


class Text:
    def __init__(self, **kw):
        """
        :font_name: name of the font
        :text: the text value
        :size: font size
        :bold: specifies if the font is bold
        :italic:  specifies if the font is italic
        :antialias: specifies if the font has antialiasing
        :color: the font color
        :background: the font background (color?)
        """

        self._text = kw.get('text', '')
        self._antialias = kw.get('antialias', False)
        self._font_name = kw.get('font_name', 'Arial')
        self._bold = kw.get('bold', False)
        self._italic = kw.get('italic', False)
        self._color = kw.get('color', Color('white'))
        self._size = kw.get('size', 16)
        self._background = kw.get('background')
        self._render: Surface = None
        self._needs_sysfont_update = True
        self._needs_render_update = True

        self.last_text = self.text
        self.font: PyGameFont = None

        self.update_sysfont()
        self.update_render()

    def update_sysfont(self):
        self.font = SysFont(self.font_name, self.size, self.bold, self.italic)
        self._needs_sysfont_update = False

    def update_render(self):
        self._render = self.font.render(self.text, self.antialias, self.color, self.background)
        self._needs_render_update = False

    @property
    def text_size(self):
        return self.font.size(self.text)

    @property
    def render(self):
        if self._needs_render_update:
            self.update_render()

        if self._needs_sysfont_update:
            self.update_sysfont()

        return self._render

    @property
    def needs_sysfont_update(self):
        return self._needs_sysfont_update

    @needs_sysfont_update.setter
    def needs_sysfont_update(self, value):
        assert isinstance(value, bool), 'new needs_sysfont_update value must be a bool'
        if not self._needs_render_update and value:
            self._needs_render_update = value
        self._needs_sysfont_update = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if not isinstance(value, str):
            value = str(value)
        self._text = value
        self._needs_render_update = True

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        assert isinstance(value, (int, float)), 'new size value must be a int or float'
        self._size = value
        self._needs_sysfont_update = True

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        assert isinstance(value, (Color, tuple, list)), 'new color value must be a Color, or RBG tuple'
        self._color = value
        self._needs_render_update = True

    @property
    def italic(self):
        return self._italic

    @italic.setter
    def italic(self, value):
        assert isinstance(value, bool), 'new italic value must be a bool'
        self._italic = value
        self._needs_sysfont_update = True

    @property
    def bold(self):
        return self._bold

    @bold.setter
    def bold(self, value):
        assert isinstance(value, bool), 'new bold value must be a bool'
        self._bold = value
        self._needs_sysfont_update = True

    @property
    def font_name(self):
        return self._font_name

    @font_name.setter
    def font_name(self, value):
        assert isinstance(value, str), 'new font_name must be a str'
        self._font_name = value
        self._needs_sysfont_update = True

    @property
    def antialias(self):
        return self._antialias

    @antialias.setter
    def antialias(self, value):
        assert isinstance(value, bool), 'new antialias value must be a bool'
        self._antialias = value
        self._needs_sysfont_update = True

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        assert isinstance(value, (Color, tuple, list)), 'new background must be a Color/RBG tuple or list'
        self._background = value
        self._needs_render_update = True


class FontCache:
    def __init__(self, **fonts):
        """
        :param fonts: name/Font value pairs
        """
        self._cache: Dict[Any, Text] = fonts

    def update(self, name, font: Text):
        """updates """
        self._cache[name] = font

    def get_text(self, name, default=''):
        if name in self:
            return self[name].text
        return default

    def set_text(self, name, new_text, append=False):
        if not isinstance(new_text, str):
            new_text = str(new_text)

        if name not in self:
            return

        if append:
            self[name].text += new_text
        else:
            self[name].text = new_text

    def get_render(self, name):
        if name in self:
            return self[name].render

    def set_color(self, name, value):
        if name in self:
            self[name].color = value

    def set_size(self, name, value, add=False):
        if name not in self:
            return

        if add:
            self[name].size += value
        else:
            self[name].size = value

    def set_bold(self, name, value):
        if name in self:
            self[name].bold = value

    def set_italic(self, name, value):
        if name in self:
            self[name].italic = value

    def set_antialias(self, name, value):
        if name in self:
            self[name].antialias = value

    def rerender(self, name):
        if name in self:
            self[name].update_render()

    def rerender_all(self):
        for font in self:
            font.update_render()

    def __contains__(self, item):
        return item in self._cache

    def __iter__(self):
        yield from self._cache

    def __getitem__(self, item):
        return self._cache.get(item)

    def __setitem__(self, key, value):
        self._cache[key] = value

    def __delitem__(self, key):
        if key in self:
            del self._cache[key]
