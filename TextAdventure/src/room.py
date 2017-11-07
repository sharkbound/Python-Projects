from typing import List

from enums.direction import Direction
from src.command import Command
from src.interactable import Interactable


class Room:
    def __init__(self, name, interactables: List[Interactable], **kwargs):
        self.interactables = interactables
        self.name = name
        self.side_rooms = {
            Direction.FORWARD: kwargs.get('forward'),
            Direction.BACK: kwargs.get('back'),
            Direction.LEFT: kwargs.get('left'),
            Direction.RIGHT: kwargs.get('right')
        }

    def get_input(self):
        print(self.get_info() + '\n\n')
        return input('>>> ')

    def get_info(self):
        return ''

    def interact(self, cmd: Command):
        pass

    def inspect(self):
        pass

    def on_enter(self):
        pass

    def on_leave(self):
        pass

    def get_side_room(self, direction: Direction):
        return self.side_rooms[direction]
