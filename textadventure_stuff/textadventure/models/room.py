from typing import List

from textadventure.enums import Direction
from .command import Command
from .interactable import Interactable


class Room:
    def __init__(self, room_id, name, interactables: List[Interactable], **kwargs):
        self.interactables = interactables
        self.room_id = room_id
        self.name = name.lower()
        self.side_rooms = {
            Direction.FORWARD: kwargs.get('forward'),
            Direction.BACK: kwargs.get('back'),
            Direction.LEFT: kwargs.get('left'),
            Direction.RIGHT: kwargs.get('right')
        }

    @property
    def input(self):
        return input('>>> ')

    @property
    def info(self):
        return ''

    @property
    def interactables_str(self):
        if not self.interactables:
            return 'you look around the room, it is empty'

        objects_str = '\n\t'.join(o.name for o in self.interactables)
        return f'you look around the room and see these objects: \n\t{objects_str}'

    def interact(self, cmd: Command):
        obj = ([x for x in self.interactables if x.name == cmd.object_name] or [None])[0]
        if obj:
            obj.on_activated()
            obj.interact()
            obj.on_deactivated()

    def inspect(self):
        pass

    def on_enter(self):
        pass

    def on_leave(self):
        pass

    def get_side_room(self, direction: Direction):
        return self.side_rooms[direction]
