from enum import Enum, auto


class CommandType(Enum):
    INVALID = auto()
    NOTHING = auto()
    LOOK = auto()
    INTERACT = auto()
    HELP = auto()
    LEFT = auto()
    RIGHT = auto()
    FORWARD = auto()
    BACK = auto()
    LIST_INTERACTABLES = auto()
