from enum import Enum
from pygame.math import Vector2
import pygame


# from main import player


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MoveDirection(Enum):
    up = 1
    down = 2
    left = 3
    right = 4


class TailPiece:
    def __init__(self, offset_x, offset_y, x=0, y=0):
        self.offset = Position(offset_x, offset_y)
        self.pos = Position(x, y)


class Player:
    def __init__(self, start_x, start_y, x_limit, y_limit, player_size):
        # self.position = Position(start_x, start_y)
        self.position = Vector2()
        self.position.x, self.position.y = start_x, start_y
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.next_position = (0, 0)
        self.tail_pieces = []
        self.hitbox_rect = pygame.Rect(start_x, start_y, player_size[0], player_size[1])

    def check_if_in_bounds(self):
        if self.position.x < 0:
            self.position.x = self.x_limit

        elif self.position.x > self.x_limit:
            self.position.x = 0

        elif self.position.y < 0:
            self.position.y = self.y_limit

        elif self.position.y > self.y_limit:
            self.position.y = 0

        self.hitbox_rect.x = self.position.x
        self.hitbox_rect.y = self.position.y

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

    @staticmethod
    def return_moved_player(pos, move_dir, change=5):
        if move_dir == MoveDirection.up:
            pos.y -= change

        elif move_dir == MoveDirection.down:
            pos.y += change

        elif move_dir == MoveDirection.left:
            pos.x -= change

        elif move_dir == MoveDirection.right:
            pos.x += change

        return pos

    def add_to_tail(self, move_direction, offset_amount=2):
        if move_direction == MoveDirection.up:
            self.tail_pieces.append(
                TailPiece(offset_y=offset_amount, offset_x=0)
            )

        elif move_direction == MoveDirection.down:
            self.tail_pieces.append(
                TailPiece(offset_y=-offset_amount, offset_x=0)
            )

        elif move_direction == MoveDirection.left:
            self.tail_pieces.append(
                TailPiece(offset_y=0, offset_x=offset_amount)
            )

        elif move_direction == MoveDirection.right:
            self.tail_pieces.append(
                TailPiece(offset_y=0, offset_x=-offset_amount)
            )

    def move_last_tail_to_front(self, move_direction, offset_amount=2):
        if len(self.tail_pieces) == 0: return

        search_spot = self.hitbox_rect
        if move_direction == MoveDirection.up:
            search_spot.y += 3
            if not self.check_collision(search_spot):
                self.tail_pieces[len(self.tail_pieces) - 1].pos.x = search_spot.x
                self.tail_pieces[len(self.tail_pieces) - 1].pos.y = search_spot.y
                # self.tail_pieces[len(self.tail_pieces) - 1].pos.x = search_spot.x
                # self.tail_pieces[len(self.tail_pieces) - 1].pos.y = search_spot.y

        elif move_direction == MoveDirection.down:
            search_spot.y -= 3
            if not self.check_collision(search_spot):
                self.tail_pieces[len(self.tail_pieces) - 1].pos.x = search_spot.x
                self.tail_pieces[len(self.tail_pieces) - 1].pos.y = search_spot.y

        elif move_direction == MoveDirection.left:
            search_spot.x += 3
            if not self.check_collision(search_spot):
                self.tail_pieces[len(self.tail_pieces) - 1].pos.x = search_spot.x
                self.tail_pieces[len(self.tail_pieces) - 1].pos.y = search_spot.y

        elif move_direction == MoveDirection.right:
            search_spot.x -= 3
            if not self.check_collision(search_spot):
                self.tail_pieces[len(self.tail_pieces) - 1].pos.x = search_spot.x
                self.tail_pieces[len(self.tail_pieces) - 1].pos.y = search_spot.y

    def check_collision(self, rect2):
        if pygame.Rect.colliderect(self.hitbox_rect, rect2):
            return True
        return False
