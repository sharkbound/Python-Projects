from pygame import *
import pygame as pg
from math import *

init()
w, h = 800, 600
S: Surface = display.set_mode((w, h))


def quit_app():
    pg.quit()
    exit()


drawn = set()


def triangle(depth, distance, pos, color):
    if depth <= 0:
        return

    depth -= 1
    y = pos[1] - distance
    p1 = pos[0] - distance, y
    p2 = pos[0] + distance, y

    pos_to_p1 = pos, p1
    if pos_to_p1 not in drawn:
        drawn.add(pos_to_p1)
        draw.line(S, color, pos, p1)
        triangle(depth, distance, p1, color)

    pos_to_p2 = pos, p2
    if pos_to_p2 not in drawn:
        drawn.add(pos_to_p2)
        draw.line(S, color, pos, p2)
        triangle(depth, distance, p2, color)

    p1_to_p2 = p1, p2
    if p1_to_p2 not in drawn:
        drawn.add(p1_to_p2)
        draw.line(S, color, p1, p2)


S.fill(Color('black'))
dist = 10
triangle(200, dist, (w // 2, h), Color('red'))
# triangle(200, dist, (w // 2, h - 5), Color('red'))

while True:
    for e in event.get():
        if e.type == QUIT:
            quit_app()

        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                quit_app()

    display.update()
