from interactables import Lamp
from textadventure.models import Room

from textadventure.util import register_room


class StartingRoom(Room):
    def __init__(self):
        super().__init__('starting', 'Starting Area', [Lamp()], right='connected')

    @property
    def info(self):
        return 'you are currently inside the starting room, to the right is another room'

    def on_leave(self):
        print('you left the starting room')

    def on_enter(self):
        print('you entered the starting room')


def setup():
    register_room(StartingRoom())
    print('registered')
