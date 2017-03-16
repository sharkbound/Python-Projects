import os

import pygame
import time
import random as r

from random import randrange, randint, uniform
from pygame import display, draw
from datetime import datetime
from patterns import patterns

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
y_max_range = 15
y_min_range = -y_max_range  # -y_max_range  - (y_max_range+4 // 2)
last_y = mid_y
draw_chance = 10
current_draw_index = len(patterns) - 1

in_game = True
draw_delay = False
randomize_color = False
force_random_color = False
clear_screen = False
require_left_mouse_held = True
left_mouse_held = False

color = (255, 0, 0)
mouse_pos = (0, 0)


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
            elif e.key == pygame.K_n:
                if current_draw_index == len(patterns) - 1:
                    current_draw_index = 0
                else:
                    current_draw_index += 1
            elif e.key == pygame.K_SPACE:
                color = random_color()
        if e.type == pygame.MOUSEMOTION:
            mouse_pos = e.pos
        if e.type == pygame.MOUSEBUTTONDOWN or e.type == pygame.MOUSEBUTTONUP and e.button == 1:
            left_mouse_held = not left_mouse_held

    # Rendering
    if require_left_mouse_held and left_mouse_held or not require_left_mouse_held:
        for o in patterns[current_draw_index]:
            draw_rect(mouse_pos[0] + o[0], mouse_pos[1] + o[1], 2, 2, color=color)

    # Updating display
    if clear_screen:
        screen.fill((0, 0, 0))
        clear_screen = False

    if draw_delay and randint(1, draw_chance) == draw_chance:
        pygame.display.update()
    else:
        display.update()
    display.set_caption(str(clock.get_fps()))
    clock.tick(60_0000)
