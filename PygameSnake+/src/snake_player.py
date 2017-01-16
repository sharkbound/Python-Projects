from enum import Enum
from pygame.math import Vector2
import pygame, colors as color


# from main import player


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)


class MoveDirection(Enum):
    up = 1
    down = 2
    left = 3
    right = 4


class TailPiece:
    def __init__(self, x=0, y=0):  # , offset_x, offset_y
        # self.offset = Position(offset_x, offset_y)
        self.pos = Position(x, y)


class Player:
    def __init__(self, start_x, start_y, x_limit, y_limit, player_size, screen=None):
        # self.position = Position(start_x, start_y)
        self.position = Vector2()
        self.position.x, self.position.y = start_x, start_y
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.next_position = (0, 0)  # Position(0, 0)
        self.tail_segments = []
        self.hitbox_rect = pygame.Rect(start_x, start_y, player_size[0], player_size[1])
        self.screen = screen

    def check_if_in_bounds(self):
        if self.position.x < 0:
            self.position.x = self.x_limit

        elif self.position.x > self.x_limit:
            self.position.x = 0

        elif self.position.y < 0:
            self.position.y = self.y_limit

        elif self.position.y > self.y_limit:
            self.position.y = 0

        # self.hitbox_rect.x = self.next_position[0]
        # self.hitbox_rect.y = self.next_position[1]

    def update_hitbox(self, new_x=0, new_y=0, new_x_offset=0, new_y_offset=0, mode=''):
        if mode == 'offset':
            self.hitbox_rect.x = self.hitbox_rect.x + new_x_offset
            self.hitbox_rect.y = self.hitbox_rect.y + new_y_offset
        elif mode == 'set':
            self.hitbox_rect.x = new_x
            self.hitbox_rect.y = new_y
        elif mode == 'next_pos':
            self.hitbox_rect.x = self.next_position[0]
            self.hitbox_rect.y = self.next_position[1]
        else:
            self.hitbox_rect.x = self.position.x
            self.hitbox_rect.y = self.position.y
            print(f'x: {self.position.x}, y: {self.position.y}')



    def move(self, direction, change=5):
        if direction == MoveDirection.up:
            self.position.y -= change

        elif direction == MoveDirection.down:
            self.position.y += change

        elif direction == MoveDirection.left:
            self.position.x -= change

        elif direction == MoveDirection.right:
            self.position.x += change

        self.check_if_in_bounds()
        # print(f'Player x: {self.position.x}, Player y: {self.position.y}')

    # def move_to_next_position(self, time):
    #     player.position = Vector2.lerp(player.position, player.next_position, time)

    def add_to_tail(self, move_direction, offset_amount=2):
        last_segment = None
        if self.get_tail_length() == 0:
            last_segment = TailPiece(self.position.x, self.position.y)
        else:
            last_segment = self.get_last_tail_segment()

        if move_direction == MoveDirection.up:
            self.tail_segments.append(
                TailPiece(last_segment.pos.x, last_segment.pos.y + offset_amount)
            )

        elif move_direction == MoveDirection.down:
            self.tail_segments.append(
                TailPiece(last_segment.pos.x, last_segment.pos.y - offset_amount)
            )

        elif move_direction == MoveDirection.left:
            self.tail_segments.append(
                TailPiece(last_segment.pos.x + offset_amount, last_segment.pos.y)
            )

        elif move_direction == MoveDirection.right:
            self.tail_segments.append(
                TailPiece(last_segment.pos.x - offset_amount, last_segment.pos.y)
            )

    def move_last_tail_to_front(self, move_direction, offset_amount=2, debug=False):
        if len(self.tail_segments) == 0: return
        t_piece = self.get_last_tail_segment()
        search_spot = self.hitbox_rect
        debug=debug
        if move_direction == MoveDirection.up:
            search_spot.y += offset_amount
            self._draw_search_spot(search_spot, debug=debug)

            if not self.check_collision(search_spot):
                print('working!')
                self.tail_segments[len(self.tail_segments) - 1].pos.x = search_spot.x
                self.tail_segments[len(self.tail_segments) - 1].pos.y = search_spot.y

        elif move_direction == MoveDirection.down:
            search_spot.y -= offset_amount
            self._draw_search_spot(search_spot, debug=debug)

            if not self.check_collision(search_spot):
                self.tail_segments[len(self.tail_segments) - 1].pos.x = search_spot.x
                self.tail_segments[len(self.tail_segments) - 1].pos.y = search_spot.y

        elif move_direction == MoveDirection.left:
            search_spot.x += offset_amount
            self._draw_search_spot(search_spot, debug=debug)

            if not self.check_collision(search_spot):
                self.tail_segments[len(self.tail_segments) - 1].pos.x = search_spot.x
                self.tail_segments[len(self.tail_segments) - 1].pos.y = search_spot.y

        elif move_direction == MoveDirection.right:
            search_spot.x -= offset_amount
            self._draw_search_spot(search_spot, debug=debug)

            if not self.check_collision(search_spot):
                self.tail_segments[len(self.tail_segments) - 1].pos.x = search_spot.x
                self.tail_segments[len(self.tail_segments) - 1].pos.y = search_spot.y

    def check_collision(self, rect2, rect1=None):
        if rect1 == None: rect1 = self.hitbox_rect
        if pygame.Rect.colliderect(rect1, rect2):
            return True
        return False

    def _draw_search_spot(self, spot, debug=False):
        pass
        # if debug:
        #     pygame.draw.rect(self.screen, color.blue, [spot.x, spot.y, 10, 10])
        #     pygame.display.update()

    def get_last_tail_segment(self):
        if len(self.tail_segments) == 0: return
        return self.tail_segments[len(self.tail_segments) - 1]

    def get_tail_length(self):
        return len(self.tail_segments)

        # @staticmethod
        # def return_moved_player(pos, move_dir, move_dict, change=5):
        #     if move_dir == MoveDirection.up or move_dir == MoveDirection.down:
        #         pos.y += move_dict[move_dir]
        #
        #     elif move_dir == MoveDirection.left or move_dir == MoveDirection.right:
        #         pos.x += move_dict[move_dir]
        #
        #     return pos
