from enum import Enum

import pygame


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MoveDirection(Enum):
    up = 1
    down = 2
    left = 3
    right = 4


class Player:
    def __init__(self, start_x, start_y, x_limit, y_limit):
        self.position = Position(start_x, start_y)
        self.x_limit = x_limit
        self.y_limit = y_limit

    def _check_if_in_bounds(self):
        if self.position.x < 0:
            self.position.x = self.x_limit

        elif self.position.x > self.x_limit:
            self.position.x = 0

        elif self.position.y < 0:
            self.position.y = self.y_limit

        elif self.position.y > self.y_limit:
            self.position.y = 0

    def move(self, direction, change=5):
        if direction == MoveDirection.up:
            self.position.y -= change

        elif direction == MoveDirection.down:
            self.position.y += change

        elif direction == MoveDirection.left:
            self.position.x -= change

        elif direction == MoveDirection.right:
            self.position.x += change

        self._check_if_in_bounds()
        # print(f'Player x: {self.position.x}, Player y: {self.position.y}')

    @staticmethod
    def return_moved_player(pos, move_dir, change = 5):
        if move_dir == MoveDirection.up:
            pos.y -= change

        elif move_dir == MoveDirection.down:
            pos.y += change

        elif move_dir == MoveDirection.left:
            pos.x -= change

        elif move_dir == MoveDirection.right:
            pos.x += change

        return pos