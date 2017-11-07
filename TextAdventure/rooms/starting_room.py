from interactables.test_interactable import Lamp
from src.command import Command
from src.room import Room


class StartingRoom(Room):
    def __init__(self):
        from rooms.connecting_room_test import ConnectedRoom
        super().__init__('Starting Area', [Lamp()], right=ConnectedRoom(self))

    def get_info(self):
        return 'you are currently inside the starting room, it seems empty right now for testings'

    def interact(self, cmd: Command):
        obj = ([x for x in self.interactables if x.name == cmd.object_name] or [None])[0]
        if obj:
            obj.on_activated()
            obj.interact()
            obj.on_deactivated()

    def on_leave(self):
        print('you left the starting room')

    def on_enter(self):
        print('you entered the starting room')

