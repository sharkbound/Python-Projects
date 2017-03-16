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
draw_index = 0  # len(patterns.pattern_list) - 1
draw_modifier = 1
FPS = 0

in_game = True
draw_delay = False
randomize_color = False
force_random_color = False
clear_screen = False
require_left_mouse_held = True
left_mouse_held = False
update_bg_color = False
reset_bg_color = False

color = (255, 0, 0)
bg_color = (0, 0, 0)
mouse_pos = (0, 0)
# mouse_c = (-10, -10)

text_to_render = [
    {
        "name": "draw_mod",
        "font": pygame.font.SysFont(name='Times New Roman', size=15),
        "clear_h": 15,
        "clear_w": 125,
        "color": (0, 255, 0),
        "draw_pos": (screen_size[0] // 2 - 50, 10),
        "text": "Draw multiplier: {0}"
    }
]


def draw_rect(x, y, width=1, height=1, color=(255, 0, 0)):
    draw.rect(screen, color, [x, y, width, height])


def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def apply_draw_mod():
    if draw_modifier == 0:
        return 1
    return draw_modifier


def l_shift_pressed():
    return pygame.key.get_mods() & pygame.KMOD_LSHIFT


def l_ctrl_pressed():
    return pygame.key.get_mods() & pygame.KMOD_LCTRL


if __name__ == '__main__':

    # game loop
    while in_game:
        # Event handling
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                in_game = False

            # key press event handling
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    in_game = False
                elif e.key == pygame.K_r:
                    reset_bg_color = True
                elif e.key == pygame.K_n:
                    draw_index = draw_index + 1 if draw_index < len(patterns.pattern_list) - 1 else 0
                elif e.key == pygame.K_SPACE:
                    color = random_color()
                elif e.key == pygame.K_c:
                    force_random_color = not force_random_color
                elif e.key == pygame.K_f:
                    update_bg_color = True
                elif e.key == pygame.K_MINUS and draw_modifier != 0:
                    draw_modifier -= 1
                elif e.key == pygame.K_EQUALS:
                    draw_modifier += 1
                elif e.key == pygame.K_LEFTBRACKET:
                    if l_shift_pressed() and l_ctrl_pressed():
                        draw_modifier -= 20
                    elif l_shift_pressed():
                        draw_modifier -= 10
                    else:
                        draw_modifier -= 5
                    if draw_modifier < 0: draw_modifier = 0
                elif e.key == pygame.K_RIGHTBRACKET:
                    if l_shift_pressed() and l_ctrl_pressed():
                        draw_modifier += 20
                    elif l_shift_pressed():
                        draw_modifier += 10
                    else:
                        draw_modifier += 5

            if e.type == pygame.MOUSEMOTION:
                mouse_pos = e.pos

            if e.type == pygame.MOUSEBUTTONDOWN or e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                left_mouse_held = not left_mouse_held

        # Randomize Color
        if force_random_color:
            color = random_color()

        # Rendering shapes
        if require_left_mouse_held and left_mouse_held or not require_left_mouse_held:
            p = patterns.get_pattern_at(draw_index)
            s = p.size if draw_modifier != 0 else (1, 1)
            s = s[0] * apply_draw_mod(), s[1] * apply_draw_mod()

            for point in p.points:
                draw_rect(mouse_pos[0] + point[0], mouse_pos[1] + point[1], s[0],
                          s[1], color=color)

        # Rendering text
        for f in text_to_render:
            draw_color = f['color']
            render_text = f['text']
            fill_x, fill_y = f['draw_pos'][0], f['draw_pos'][1] + 3

            if 'random' in draw_color: draw_color = random_color()
            if 'multiplier' in render_text.lower():
                render_text = render_text.format(draw_modifier)

            label = f['font'].render(render_text, 1, draw_color)
            draw_rect(fill_x, fill_y, len(render_text) * 7, f['clear_h'], color=bg_color)
            screen.blit(label, f['draw_pos'])

        # Updating display
        if update_bg_color:
            update_bg_color = False
            clear_screen = True
            bg_color = random_color()

        if reset_bg_color:
            reset_bg_color = False
            clear_screen = True
            bg_color = (0, 0, 0)

        if clear_screen:
            screen.fill(bg_color)
            clear_screen = False

        if draw_delay and randint(1, draw_chance) == draw_chance:
            pygame.display.update()
        else:
            display.update()

        FPS = int(clock.get_fps())
        display.set_caption(f'FPS: {FPS}')
        clock.tick(60_0000)
