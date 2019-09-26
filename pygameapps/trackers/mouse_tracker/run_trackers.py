from numpy import clip
from pygame import *
from pygame.draw import *
from pygame.colordict import THECOLORS
from pygame.display import *

from pygame_util import get_clock, random_color
from pygameapps.trackers.classes import Position
from utils.dotdict import DotDict

init()

SIZE = (600, 600)
S = set_mode(SIZE)
CENTER = SIZE[0] // 2, SIZE[1] // 2
CLOCK = get_clock()
DISTANCE = 100
SPEED = 10

colors = DotDict(THECOLORS)
obj = Position(0, 0)

joystick.init()
joy = joystick.Joystick(0)
joy.init()

while True:
    for e in event.get():
        if e.type == QUIT:
            exit()
        elif e.type == KEYDOWN:
            if e.key == K_q:
                exit()
        elif e.type == JOYAXISMOTION:
            print(f'JOY {e.joy} AXIS {e.axis} VALUE {e.value}')
        elif e.type == JOYBUTTONDOWN:
            print(e.button)

    force = Vector2(CENTER) - mouse.get_pos()
    force.x, force.y = clip(-force.x, -SPEED, SPEED), clip(-force.y, -SPEED, SPEED)

    obj.move(relx=force.x, rely=force.y)
    obj.keep_in_bounds(SIZE, loop=False)

    circle(S, random_color(), obj.pos, 5)
    circle(S, colors.orange, CENTER, 30, 1)

    update()
    CLOCK.tick(30)
