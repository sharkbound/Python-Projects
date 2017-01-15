# from pygame import QUIT, KEYDOWN, KEYUP
from pygame import *
from snake_player import MoveDirection as move

import pygame, sys


class EventParser:
    # def __init__(self, GUI):
    #     self.gui = GUI

    def parse(self, event, screen=None, player=None):
        if event.type == QUIT:
            pygame.quit()
            # sys.exit()

        elif event.type == KEYUP:
            key_name = pygame.key.name(event.key)

        elif event.type == KEYDOWN:
            key_name = pygame.key.name(event.key)

            if key_name == 'escape':
                pygame.quit()
                sys.exit()

    def parse_movement(self, last_dir, event):
        if event.type != pygame.KEYDOWN:
            return last_dir

        if event.key == K_w or event.key == K_UP:
            return move.up

        elif event.key == K_s or event.key == K_DOWN:
            return move.down

        elif event.key == K_a or event.key == K_LEFT:
            return move.left

        elif event.key == K_d or event.key == K_RIGHT:
            return move.right

        else:
            return last_dir
