import pygame

from pygame import display, draw, math as pmath, QUIT, KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame.math import Vector2

from data.colors import Colors

screen_size = (600, 600)

game = pygame.init()
screen = display.set_mode(screen_size)
clock = pygame.time.Clock()

def vector2_to_int_tuple(vector2):
    return (int(vector2.x), int(vector2.y))

def main_loop():
    mouse_pos = Vector2()
    cur_pos = Vector2()
    momentum_move_speed = 0.001
    dist_to_mouse = 0.0
    fill_color = (0, 0, 0)
    lerp_time = 0.001

    cur_pos.x, cur_pos.y = screen_size[0] / 2, screen_size[1] / 2

    while True:
        # Event handling
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                break

            if e.type == MOUSEMOTION:
                mouse_pos.x, mouse_pos.y = e.pos[0], e.pos[1]
                dist_to_mouse = cur_pos.distance_to(mouse_pos)

            if e.type == KEYDOWN:
                pass

        # Updating variables
        cur_pos = cur_pos.lerp(mouse_pos, lerp_time)

        print(dist_to_mouse)

        # Filling Screen
        screen.fill(Colors.BLACK)

        # Rendering
        # draw.rect(screen, (255, 0, 0), [cur_pos.x, cur_pos.y, 10, 10])
        draw.circle(screen, Colors.GREEN, vector2_to_int_tuple(cur_pos), 5)

        # Updating Screen
        display.update()


if __name__ == '__main__':
    main_loop()
