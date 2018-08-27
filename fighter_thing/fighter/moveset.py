from __future__ import annotations

from typing import Callable, Optional


class MoveSet:
    def __init__(self, *moves: Move):
        self.moves = moves

    def _filter(self, predicate: Callable[[Move], bool]):
        for move in self.moves:
            if predicate(move):
                return move

    def __getitem__(self, item) -> Optional[Move]:
        if isinstance(item, str):
            return self._filter(lambda m: item in (m.id, m.name))

        raise TypeError(f'expected type {str}, got {type(item)}')


class Move:
    def __init__(self, id, dmg, desc='', name: str = None):
        self.id = id
        self.name = name or id
        self.desc = desc
        self.dmg = dmg
