import re
from dataclasses import dataclass, field
from itertools import chain, islice
from random import randint
from typing import List, Iterable, Dict, Union


@dataclass(frozen=True)
class RollResult:
    dice: 'Die' = field(repr=False)
    total: int
    rolls: List[int]


@dataclass(frozen=True)
class Die:
    id: str
    times: int
    sides: int

    def roll(self):
        rolls = [randint(1, self.sides) for _ in range(self.times)]
        return RollResult(total=sum(rolls), rolls=rolls, dice=self)

    def __str__(self):
        return self.id


class DiceCollection:
    def __init__(self, *dice_strings: str, keep_previous=False):
        self.keep_previous = keep_previous
        self.dice: Dict[str, Die] = {}
        self.previous: List[RollResult] = []

        self._parse(dice_strings)

    def roll(self, start=0, stop=None, step=1):
        return self._append_to_previous(
            [dice.roll() for dice in islice(self.dice.values(), start, stop, step)])

    def _append_to_previous(self, rolls: List[RollResult]):
        if self.keep_previous:
            self.previous.append(rolls)
        return rolls

    def _parse(self, dice_strings: Iterable[str]):
        for string in chain.from_iterable((string.split() for string in dice_strings)):
            for dice_id, times, sides in self._parse_dice_info(string):
                die = Die(id=dice_id, times=times, sides=sides)
                self.dice[die.id] = die

    def _parse_dice_info(self, dice_info: str):
        yield from ((f'{times}d{sides}', int(times), int(sides))
                    for times, sides in re.findall(r'(\d+)[Dd](\d+)', dice_info))

    def __getitem__(self, item: Union[slice, str]):
        if isinstance(item, str):
            return self._append_to_previous([self.dice[item].roll()])

        if item.stop is not None and item.stop < 0:
            stop = max(len(self.dice) + item.stop, 0)
        else:
            stop = item.stop

        start = item.start or 0
        return self.roll(start, stop, item.step)

    def __str__(self):
        pairs = ' '.join(dice.id for dice in self.dice.values())
        return f'<{self.__class__.__name__} {pairs}>'


if __name__ == '__main__':
    all_dice = DiceCollection('1d4', '8d4', '9d3', '8d3')
    print(*all_dice[::2], all_dice, sep='\n')
