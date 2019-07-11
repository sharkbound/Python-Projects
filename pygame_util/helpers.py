import copy
from random import *
from decimal import Decimal

from math import cos, radians, sin
from typing import Union, Tuple

from pygame.event import Event
from pygame.math import Vector2

from pygame import *
import pygame

from pygame_util import settings

try:
    from .data import Point
except ImportError:
    Point = Vector2


# ------------
#    SETUP
# ------------


def setup(window_size=(600, 600), flags=0, depth=0) -> Surface:
    init()
    settings.size = window_size
    settings.surface = display.set_mode(window_size, flags, depth)
    return settings.surface


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
    center = (settings.size[0] // 2 if int_div else settings.size[0] / 2,
              settings.size[1] // 2 if int_div else settings.size[1] / 2)
    if axis:
        return center[axis]
    return center


def get_width():
    return settings.size[0]


def get_height():
    return settings.size[1]


def fill_screen(color='black', rect=None):
    settings.surface.fill(to_color(color), rect)


def random_pos(padding=1, max_x: int = None, max_y: int = None) -> Tuple[int, int]:
    if max_x is None:
        max_x = settings.size[0]
    if max_y is None:
        max_y = settings.size[1]

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


def random_color():
    return Color(randrange(256), randrange(256), randrange(256))


def update():
    display.update()


def blit(item, dest, area=None, special_flags=0):
    settings.surface.blit(item, dest, area, special_flags)


def get_surface():
    return settings.surface


def keep_in_bounds_rect(rect: Rect, bounds=None):
    if bounds is None:
        bounds = settings.size

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
        bounds = settings.size

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
        bounds = settings.size

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
        bounds = settings.size

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
    draw.rect(settings.surface, color, rect, width)


def draw_rect(color, x, y, lenx, leny, width=0):
    draw.rect(settings.surface, to_color(color), (x, y, lenx, leny), width)


def draw_square(color, x, y, size, width=0):
    draw.rect(settings.surface, to_color(color), (x, y, size, size), width)


def draw_circle(color, pos, radius, width=0):
    draw.circle(settings.surface, to_color(color), tuple(map(int, pos)), radius, width)


def draw_line(color, start_pos, end_pos, width=1):
    draw.line(settings.surface, to_color(color), start_pos, end_pos, width)


def draw_lines(color, closed, pointlist, width=1):
    draw.lines(settings.surface, to_color(color), closed, pointlist, width)


def draw_connecting_lines(color, pointlist, width=1):
    last = pointlist[0]
    for p in pointlist[1:]:
        draw_line(color, last, p, width)
        last = p


def draw_poly(color, pointlist, width=0):
    draw.polygon(settings.surface, to_color(color), pointlist, width)


def draw_aaline(color, startpos, endpos, blend=1):
    draw.aaline(settings.surface, to_color(color), startpos, endpos, blend)


# -------
#  COLOR
# -------
def to_color(*args):
    if len(args) == 1:
        value = args[0]
        if isinstance(value, Color):
            return value
        elif isinstance(value, str):
            return Color(value)
        elif isinstance(value, (tuple, list)):
            return Color(*value)
        raise TypeError(f'invalid type: {type(value)}')
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


def randforce(min_force, max_force):
    return uniform(min_force, max_force), uniform(min_force, max_force)


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


def to_grid(pos, grid_size):
    if isinstance(grid_size, (int, float, Decimal)):
        x_width = y_width = grid_size
    else:
        x_width, y_width = grid_size

    if isinstance(pos, tuple):
        return (round(pos[0] / x_width) * x_width, round(pos[1] / y_width) * y_width)

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
