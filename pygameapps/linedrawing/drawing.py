from pygame.draw import *
from pygame.display import set_mode, update, set_caption, flip
from pygame import event, colordict
from pygame import *
import pygame as pg
from utils.dotdict import DotDict

init()
SIZE = 600, 600
S = set_mode(SIZE)
COLORS = DotDict(colordict.THECOLORS)

dragging = False
all_lines = []

while True:
    for e in event.get():
        if e.type == QUIT or e.type == KEYDOWN and e.type == K_q:
            pg.quit()
            exit()
        elif e.type == MOUSEMOTION:
            if all_lines and dragging:
                all_lines[-1].append(e.pos)
        elif e.type == MOUSEBUTTONDOWN:
            all_lines.append([])
            dragging = True
        elif e.type == MOUSEBUTTONUP:
            dragging = False

    for line in all_lines:
        if len(line) > 1:
            lines(S, COLORS.green, False, line)

    update()
