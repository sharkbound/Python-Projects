from enum import Enum, auto


class Result(Enum):
    INCREMENT_PTR = auto()
    NOTHING = auto()


DEFAULT_RESULT = Result.INCREMENT_PTR
