from enum import Enum, auto


class GameAction(Enum):
    NOTHING = auto()
    GO_TO_PREVIOUS_ROOM = auto()
    GAME_OVER = auto()