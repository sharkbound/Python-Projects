from pygame import QUIT, KEYDOWN, KEYUP
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

        key_name = pygame.key.name(event.key)
        if key_name == 'w' or key_name == 'up':
            return move.up

        elif key_name == 's' or key_name == 'down':
            return move.down

        elif key_name == 'a' or key_name == 'left':
            return move.left

        elif key_name == 'd' or key_name == 'right':
            return move.right