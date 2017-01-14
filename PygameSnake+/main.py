import sys
import pygame
import colors as color

from guihelper import Gui
from event_manager import EventParser
from snake_player import Player, MoveDirection as MoveDir, TailPiece
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
player_hitbox_size = (10, 10)
apple_size = (20, 20)
last_appended_tailpiece = TailPiece(0, 0)

gui = Gui(pygame.display.set_mode(screen_size))
parser = EventParser()
player = Player(screen_size[0] / 2, screen_size[1] / 2, screen_size[0], screen_size[1], player_hitbox_size)
apples = Apple.create_rand_apple_list(30, color.blue, (limit_x, limit_y), apple_size)
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

    # checking for collisions...
    for a in apples:
        if player.check_collision(a.hitbox_rect):
            player.add_to_tail(last_dir)
            a.reset()
    # endregion

    # region rendering
    gui.background_fill(color.black)

    for a in apples:
        pygame.draw.rect(gui.screen, color.red, [a.position.x, a.position.y, apple_size[0], apple_size[1]])
        # pygame.draw.rect(gui.screen, color.green, a.hitbox_rect) #renders apples hitbox

    for piece in player.tail_pieces:
        pygame.draw.rect(gui.screen, color.tan, [piece.pos.x, piece.pos.y, 10, 10])

    pygame.draw.rect(gui.screen, color.dark_tan, [player.position.x, player.position.y, player_size[0], player_size[1]])
    # pygame.draw.rect(gui.screen, color.green, player.hitbox_rect) #renders the players snake head hitbox as a green square

    gui.update()
    clock.tick(120)  # fps limit
    # print('fps:', clock.get_fps())
    # endregion

    player.move_last_tail_to_front(last_dir)
