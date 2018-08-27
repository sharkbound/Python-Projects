from __future__ import annotations

from copy import deepcopy
from random import randint, choice

from .moveset import MoveSet, Move


class Fighter:
    def __init__(self, name, moves=None, max_hp=100, attack=None, speed=1):
        self.moves = moves or MoveSet()
        self.speed = speed
        self.attack = attack if attack is not None else randint(1, 5)
        self.max_hp = max_hp
        self.name = name
        self.hp = max_hp

    def calculate_damage(self, src: Fighter, move: Move):
        return move.dmg

    def damage(self, src: Fighter, move: Move):
        dmg = self.calculate_damage(src, move)
        self.hp -= dmg
        return dmg

    def damage_raw(self, move: Move):
        self.hp -= move.dmg
        return move.dmg

    def copy(self) -> Fighter:
        return deepcopy(self)

    @property
    def alive(self):
        return self.hp > 0

    def get_move(self) -> Move:
        return choice(self.moves.moves)

    def __str__(self):
        return f'<Fighter name={self.name!r} hp={self.hp!r}>'

    def __eq__(self, other):
        return self.name == other.name and self.max_hp == other.max_hp and self.speed == other.speed


class Player(Fighter):
    def get_move(self) -> Move:
        while True:
            print()

            for m in self.moves.moves:
                print(f'{m.id} > {m.name} ({m.dmg} dmg)')

            move = self.moves[input('\nenter the move you want to use >>> ')]

            print()

            if move:
                return move
