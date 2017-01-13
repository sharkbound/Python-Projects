import sys
import pygame
import colors as color

from guihelper import Gui
from event_manager import EventParser
from snake_player import Player, MoveDirection as MoveDir
from apple import Apple
from pygame.math import Vector2

# region Variables
screen_size = (400, 400)
movement_distance = 0.8
in_game = False
last_dir = MoveDir.down
limit_x = screen_size[0]
limit_y = screen_size[1]
movement_lerp_time = 0.9
player_size = (10, 10)
apple_size = (20, 20)

gui = Gui(pygame.display.set_mode(screen_size))
parser = EventParser()
player = Player(screen_size[0] / 2, screen_size[1] / 2, screen_size[0], screen_size[1])
apples = Apple.create_rand_apple_list(30, color.blue, (limit_x, limit_y))
clock = pygame.time.Clock()
# endregion

gui.set_title('Snake+')
pygame.init()

while not in_game:
    # region event handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            in_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for a in apples:
                    a.reset()

        last_dir = parser.parse_movement(last_dir, event)
        parser.parse(event, player=player)
    # endregion

    # region player logic
    player.next_position = Player.return_moved_player(player.position, last_dir, change=movement_distance)
    player.position = Vector2.lerp(player.position, player.next_position, movement_lerp_time)
    player.check_if_in_bounds()

    for a in apples:
        if pygame.Rect.colliderect(
                pygame.Rect(a.position.x, a.position.y, apple_size[0], apple_size[1]),
                pygame.Rect(player.position.x, player.position.y, player_size[0], player_size[1])
        ):
            a.reset()
    # endregion

    # region rendering
    gui.background_fill(color.black)
    pygame.draw.rect(gui.screen, color.dark_tan, [player.position.x, player.position.y, player_size[0], player_size[1]])

    for a in apples:
        pygame.draw.rect(gui.screen, color.red, [a.position.x, a.position.y, apple_size[0], apple_size[1]])

    gui.update()
    clock.tick(120)  # fps limit
    # print('fps:', clock.get_fps())
    # endregion
