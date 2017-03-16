import os

import pygame
import time
import random as r
import patterns

from random import randrange, randint, uniform
from pygame import display, draw
from datetime import datetime

patterns.init_patterns()

screen_size = (600, 600)
game = pygame.init()
screen = display.set_mode(screen_size)
clock = pygame.time.Clock()

width = 2.5
height = width

draw_chance = 10
draw_index = 0 #len(patterns.pattern_list) - 1

in_game = True
draw_delay = False
randomize_color = False
force_random_color = True
clear_screen = False
require_left_mouse_held = True
left_mouse_held = False

color = (255, 0, 0)
mouse_pos = (0, 0)


def draw_rect(x, y, width=1, height=1, color=(255, 0, 0)):
    draw.rect(screen, color, [x, y, width, height])


def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


if __name__ == '__main__':

    # game loop
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
                    draw_index = draw_index + 1 if draw_index < len(patterns.pattern_list) - 1 else 0
                elif e.key == pygame.K_SPACE:
                    color = random_color()

            if e.type == pygame.MOUSEMOTION:
                mouse_pos = e.pos

            if e.type == pygame.MOUSEBUTTONDOWN or e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                left_mouse_held = not left_mouse_held

        # Randomize Color
        if (force_random_color):
            color = random_color()

        # Rendering
        if require_left_mouse_held and left_mouse_held or not require_left_mouse_held:
            p = patterns.get_pattern_at(draw_index)
            for point in p.points:
                draw_rect(mouse_pos[0] + point[0], mouse_pos[1] + point[1], p.size[0], p.size[1], color=color)

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
