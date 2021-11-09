from random import randrange

from pygame.math import Vector2
from pygame import *
from enum import Enum


class Direction(Enum):
    UP, DOWN, LEFT, RIGHT, STILL = range(5)


SCREEN_SIZE = (600, 600)
BLOCK_SIZE = 10
SPEED_INCREMENT = 0.01

BLACK = Color('black')
WHITE = Color('white')
RED = Color('red')
BLUE = Color('blue')
GREEN = Color('green')

init()
SRC: Surface = display.set_mode(SCREEN_SIZE)

CLOCK = time.Clock()
MOVE_DICT = {
    Direction.STILL: Vector2(0, 0),
    Direction.LEFT: Vector2(-BLOCK_SIZE, 0),
    Direction.RIGHT: Vector2(BLOCK_SIZE, 0),
    Direction.UP: Vector2(0, -BLOCK_SIZE),
    Direction.DOWN: Vector2(0, BLOCK_SIZE)
}
KEY_TO_MOVE = {
    K_UP: Direction.UP,
    K_DOWN: Direction.DOWN,
    K_LEFT: Direction.LEFT,
    K_RIGHT: Direction.RIGHT,
    K_SPACE: Direction.STILL
}


def to_grid_pos(p) -> Vector2:
    p.x = round((p.x / BLOCK_SIZE)) * BLOCK_SIZE
    p.y = round((p.y / BLOCK_SIZE)) * BLOCK_SIZE
    return p


def is_in_bounds(p):
    return (
            0 <= p.x < SCREEN_SIZE[0] and 0 <= p.y < SCREEN_SIZE[1]
    )


def get_random_apple():
    return to_grid_pos(Vector2(randrange(1, SCREEN_SIZE[0] - 1), randrange(1, SCREEN_SIZE[1] - 1)))


def get_center():
    return to_grid_pos(Vector2(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2))


while True:
    cur_dir = Direction.STILL
    points = [get_center()]
    tail_length = 0
    apple = get_random_apple()
    gameover = False
    frames = 0
    speed = 10

    while not gameover:
        SRC.fill(BLACK)

        for e in event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == K_ESCAPE:
                exit()
            elif e.type == KEYDOWN:
                cur_dir = KEY_TO_MOVE.get(e.key, cur_dir)
                # cheat name
                if e.key == K_n:
                    tail_length += 10

        points.append(points[-1] + MOVE_DICT[cur_dir])
        points = list(map(to_grid_pos, points[-tail_length - 1::]))

        if points[-1] == apple:
            apple = get_random_apple()
            tail_length += 1

        last = points[-1]
        if not is_in_bounds(last):
            gameover = True

        draw.rect(SRC, RED, [apple.x, apple.y, BLOCK_SIZE, BLOCK_SIZE])
        draw.rect(SRC, [0, 0, 150], [*last, BLOCK_SIZE, BLOCK_SIZE])

        if cur_dir == Direction.STILL: continue
        for p in points[:-1]:
            draw.rect(SRC, [0, 100, 0], [p.x, p.y, BLOCK_SIZE, BLOCK_SIZE])
            if p == last:
                gameover = True  # player hit his tail

        speed += SPEED_INCREMENT
        print(speed)
        display.update()
        CLOCK.tick(speed)
