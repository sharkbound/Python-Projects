from random import randint

from pygame import *
from pygame.colordict import THECOLORS
from pygame.display import *
from pygame.draw import *

from pygame_util import random_color
from pygameapps.trackers.classes import Position
from utils.dotdict import DotDict

init()
SIZE = (700, 700)
CENTER = tuple(i // 2 for i in SIZE)
S = set_mode(SIZE)
colors = DotDict(THECOLORS)

m = Position(350, 350)

while True:
    for e in event.get():
        if e.type == QUIT:
            exit()
        elif e.type == KEYDOWN:
            if e.key == K_q:
                exit()

    pos = mouse.get_pos()
    x, y = (pos[0] - CENTER[0]) % 5, (pos[1] - CENTER[1]) % 5
    m.move(relx=x, rely=y)
    m.keep_in_bounds(SIZE)
    circle(S, random_color(), m.pos, randint(1, 20))
    update()
