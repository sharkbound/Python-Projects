import pygame as pg
from random import randint
from math import radians, cos, sin

pg.init()
width, height = 800, 600
S: pg.Surface = pg.display.set_mode((width, height))
clock = pg.time.Clock()
FPS = 60


def randbyte():
    return randint(0, 255)


def randcolor(random_alpha=True):
    return pg.Color(randbyte(), randbyte(), randbyte(), randint(1, 255) if random_alpha else 255)


def find_end(pos, angle, length):
    return pos[0] * cos(radians(angle)) + length, pos[1] * sin(radians(angle)) + length


def on_key_down(e, key, char, mod):
    global redraw

    if e.key == pg.K_ESCAPE:
        quit_game()
    if key == pg.K_SPACE:
        redraw = True


def on_key_up(e, key, mod):
    pass


def on_event(e):
    if e.type == pg.QUIT:
        quit_game()

    elif e.type == pg.KEYDOWN:
        on_key_down(e, e.key, e.unicode, e.mod)

    elif e.type == pg.KEYUP:
        on_key_up(e, e.key, e.mod)


def quit_game():
    pg.quit()
    exit()


def next_color():
    cur_color[0] += 1
    cur_color[1] += 1
    cur_color[2] += 1

    cur_color[0] %= 255
    cur_color[1] %= 255
    cur_color[2] %= 255

    return cur_color


def tree(max_depth, depth, length, xc, yc, pos, base_color):
    if not depth:
        return

    rightend = pos[0] + xc + length, pos[1] + yc - length
    leftend = pos[0] - xc - length, pos[1] + yc - length
    right_points = (pos, rightend)
    left_points = (pos, leftend)

    color = next_color()

    if right_points not in drawn:
        drawn.add(right_points)
        pg.draw.line(S, color, pos, rightend, depth)
        tree(max_depth, depth - 1, length, xc, yc, rightend, base_color)

    if left_points not in drawn:
        drawn.add(left_points)
        pg.draw.line(S, color, pos, leftend, depth)
        tree(max_depth, depth - 1, length, xc, yc, leftend, base_color)


drawn = set()
md = 50
cur_color = list(randcolor())
redraw = True


def draw():
    S.fill((0, 0, 0))

    for i in range(-310, 900, 50):
        tree(md, md, 20, 5, -5, (i, height + 100), randcolor())

    pg.display.update()


while True:
    for event in pg.event.get():
        on_event(event)

    if redraw:
        cur_color = [*randcolor()]
        drawn.clear()
        draw()
        redraw = False
