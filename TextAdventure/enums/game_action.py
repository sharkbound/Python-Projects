from enum import Enum


class GameAction(Enum):
    NOTHING, GO_TO_PREVIOUS_ROOM, GAME_OVER = range(2)