from models import Room
from util import register_room


class ConnectedRoom(Room):
    def __init__(self):
        super().__init__('connected', 'ConnectedRoom', [], left='starting')

    @property
    def info(self):
        return 'it is a empty room, to the left is the starting room'

    def on_enter(self):
        print('you entered the connected room')

    def on_leave(self):
        print('you left the connected room')

def setup():
    register_room(ConnectedRoom())
    print('registered')
