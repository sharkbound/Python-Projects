from enum import Enum


class CommandType(Enum):
    INVALID, NOTHING, INSPECT, INTERACT, HELP, LEFT, RIGHT, FORWARD, BACK = range(9)