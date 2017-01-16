import pygame
import colors as color

from guihelper import Gui
from event_manager import EventParser
from snake_player import Player, MoveDirection as MoveDir, TailPiece, Position
from apple import Apple
from pygame.math import Vector2


# region Variables
def game_loop():
    screen_size = (400, 400)
    screen_middle = (screen_size[0] / 2, screen_size[1] / 2)
    in_game = True
    debug_mode = True
    last_dir = MoveDir.down
    limit_x = screen_size[0]
    limit_y = screen_size[1]
    movement_lerp_time = 0.9
    player_size = (10, 10)
    player_hitbox_size = (10, 10)
    apple_size = (20, 20)
    last_appended_tailpiece = None
    movement_distance = 0.8
    tail_placement_offset = 12
    tail_placement_offset_dict = {MoveDir.up: tail_placement_offset, MoveDir.down: -tail_placement_offset,
                                  MoveDir.left: tail_placement_offset, MoveDir.right: -tail_placement_offset}
    player_movement_vect2_dict = {MoveDir.up: Vector2(0, -movement_distance),
                                  MoveDir.down: Vector2(0, movement_distance),
                                  MoveDir.left: Vector2(-movement_distance, 0),
                                  MoveDir.right: Vector2(movement_distance, 0)}
    # hitbox_offset = player_size[0] + 1.2
    # player_hitbox_movement_raw_dict = {MoveDir.up: -hitbox_offset, MoveDir.down: hitbox_offset,
    #                                    MoveDir.left: -hitbox_offset, MoveDir.right: hitbox_offset}

    # player_movement_raw_dict = {MoveDir.up: -movement_distance, MoveDir.down: movement_distance,
    #                             MoveDir.left: -movement_distance, MoveDir.right: movement_distance}


    gui = Gui(pygame.display.set_mode(screen_size))
    parser = EventParser()
    player = Player(screen_middle[0], screen_middle[1], screen_size[0], screen_size[1], player_hitbox_size,
                    screen=gui.screen)
    apples = Apple.create_rand_apple_list(1, color.blue, (limit_x, limit_y), apple_size)
    clock = pygame.time.Clock()

    # endregion

    gui.set_title('Snake+')
    pygame.init()

    while in_game:
        # region event handling
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                in_game = True

            if event.type == pygame.KEYDOWN:

                if debug_mode:
                    if event.key == pygame.K_k:
                        player.add_to_tail(last_dir, offset_amount=10)

                    if event.key == pygame.K_SPACE:
                        for a in apples:
                            a.reset()

            last_dir = parser.parse_movement(last_dir, event)
            parser.parse(event, player=player)
        # endregion

        # region player logic
        player.next_position = player.position + player_movement_vect2_dict[last_dir]
        player.position = Vector2.lerp(player.position, player.next_position, movement_lerp_time)
        player.check_if_in_bounds()
        player.move_last_tail_to_front(last_dir, offset_amount=tail_placement_offset, debug=debug_mode)
        player.update_hitbox()

        # checking for collisions...
        for a in apples:
            if player.check_collision(a.hitbox_rect):
                player.add_to_tail(last_dir, offset_amount=10)
                a.reset()
        # endregion

        # region rendering
        gui.background_fill(color.black)

        for a in apples:
            pygame.draw.rect(gui.screen, color.red, [a.position.x, a.position.y, apple_size[0], apple_size[1]])
            if debug_mode:
                pygame.draw.rect(gui.screen, color.green, a.hitbox_rect)  # renders apples hitbox

        for piece in player.tail_segments:
            pygame.draw.rect(gui.screen, color.tan, [piece.pos.x, piece.pos.y, 10, 10])

        pygame.draw.rect(gui.screen, color.dark_tan,
                         [player.position.x, player.position.y, player_size[0], player_size[1]])

        if debug_mode:
            pygame.draw.rect(gui.screen, color.green,
                             player.hitbox_rect)  # renders the players snake head hitbox as a green square

        gui.update()
        clock.tick(120)  # fps limit
        # print('fps:', clock.get_fps())
        # endregion


if __name__ == '__main__':
    game_loop()
