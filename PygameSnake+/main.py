import sys
import pygame

from guihelper import Gui
from event_manager import EventParser
from snake_player import Player, MoveDirection as move_dir

screen_size = (600, 600)
movement_distance = 0.1
exiting = False
last_dir = move_dir.down

gui = Gui(pygame.display.set_mode(screen_size))
parser = EventParser()
player = Player(screen_size[0] / 2, screen_size[1] / 2, screen_size[0], screen_size[1])

gui.set_title('Snake+')

pygame.init()

while not exiting:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exiting = True

        # if event.type == pygame.KEYDOWN:
        #     key_name = pygame.key.name(event.key)

        last_dir = parser.parse_movement(last_dir, event)
        parser.parse(event, player=player)

    player.position = Player.return_moved_player(player.position, last_dir, change=movement_distance)
    player._check_if_in_bounds()

    if not exiting:
        gui.background_fill((255, 255, 255))
        pygame.draw.rect(gui.screen, (0, 0, 0), [player.position.x, player.position.y, 10, 10])
        gui.update()
