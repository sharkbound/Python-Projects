from enum import Enum
from random import randint
from utils.stringutil import auto_str_filtered


def rand_dial_position():
    return randint(1, 100)


def sign(i):
    return -1 if i < 0 else 0 if not i else 1


class State(Enum):
    green = 1
    red = 0


@auto_str_filtered('correct_position'.__ne__)
class Lock:
    POSITION_COUNT = 100

    def __init__(self):
        self.correct_position = rand_dial_position()
        self.current_position = 1
        self.state = State.red
        self.recorded_dial_position = self.current_position

    def rotate(self, rotation: int):
        self.current_position = (self.current_position + rotation) % self.POSITION_COUNT
        if not self.current_position:
            if rotation < 1:
                self.current_position = self.POSITION_COUNT
            else:
                self.current_position = 1

    def record(self):
        self.recorded_dial_position = self.current_position

    def recorded(self):
        return self.recorded_dial_position

    def check_green(self):
        return self.state is State.green

    def check_red(self):
        return self.state is State.red


lock = Lock()
print(lock)
print(lock.rotate(101))
