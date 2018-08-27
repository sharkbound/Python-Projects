from copy import deepcopy
from typing import Tuple
from random import choice

from .fighter import Fighter


class Fight:
    def __init__(self, *fighters: Fighter):
        self.original_fighters: Tuple[Fighter] = deepcopy(fighters)
        self.fighters: Tuple[Fighter] = deepcopy(fighters)

    @property
    def alive_fighters(self):
        yield from (f for f in self.fighters if f.alive)

    @property
    def alive_count(self):
        return sum(1 for _ in self.alive_fighters)

    def start(self) -> Fighter:
        self.fighters = sorted(deepcopy(self.original_fighters), key=lambda x: x.speed, reverse=True)

        while self.alive_count > 1:
            self._do_round()

        print(*self.alive_fighters)
        return next(self.alive_fighters)

    def _do_round(self):
        for fighter in self.alive_fighters:
            e: Fighter = choice(tuple(f for f in self.alive_fighters if f != fighter))
            move = fighter.get_move()
            dmg = e.damage(fighter, move)
            print(f'{fighter.name} hit {e.name} with {move.name}({dmg} DMG), {e.name} has {e.hp} HP remaining')

            if self.alive_count <= 1:
                return
