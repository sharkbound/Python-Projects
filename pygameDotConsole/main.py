import pygame
import time
import random as r

from random import randrange, randint, uniform
from pygame import display, draw

screen_size = (600, 600)
game = pygame.init()
screen = display.set_mode(screen_size)
clock = pygame.time.Clock()

width = 2.5
height = width

mid_x = screen_size[0] / 2
mid_y = screen_size[1] / 2
current_x = 0
change_x = 1
y_max_range = 30
y_min_range = -y_max_range  # -y_max_range  - (y_max_range+4 // 2)
last_y = mid_y
draw_chance = 10

in_game = True
draw_delay = False
randomize_color = False
clear_screen = False

color = (255, 0, 0)


def draw_rect(x, y, width=1, height=1, color=(255, 0, 0)):
    draw.rect(screen, color, [x, y, width, height])


def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


while in_game:

    # Event handling
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            in_game = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                in_game = False
            elif e.key == pygame.K_r:
                clear_screen = True

    # Calculating / Setting values
    current_x += change_x
    last_y = last_y + randrange(int(y_min_range), int(y_max_range))

    # boundary checks
    if last_y >= screen_size[1] or last_y <= 0:
        last_y = mid_y
        randomize_color = True
    if current_x >= screen_size[0] or current_x <= 0:
        current_x = 0
        randomize_color = True

    # Rendering
    if randomize_color:
        color = random_color()
        randomize_color = False

    draw_rect(current_x, last_y, int(width), int(height), color=color)

    # Updating display
    if clear_screen:
        screen.fill((0, 0, 0))
        clear_screen = False
    if draw_delay and randint(1, draw_chance) == draw_chance:
        pygame.display.update()
    else:
        display.update()
    # display.update()
    clock.tick(60)
