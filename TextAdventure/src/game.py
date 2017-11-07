from enums.command_type import CommandType
from enums.direction import Direction
from rooms.starting_room import StartingRoom
from src.command import Command
from random import choice

HELP_MSG = """Commands: 
inspect {object_name} -> inspects a object
interact {object_name} -> interacts with a object
help -> how this menu"""

INVALID_MSGS = [
    'what was that?',
    'i do not understand you',
    'invalid command',
    'm8 are you even trying?!?!!?'
]

COMMAND_TYPE_TO_DIR = {
    CommandType.FORWARD: Direction.FORWARD,
    CommandType.BACK: Direction.BACK,
    CommandType.LEFT: Direction.LEFT,
    CommandType.RIGHT: Direction.RIGHT
}


class Game:
    def __init__(self):
        self.current = StartingRoom()
        self.running = True

    def run(self):
        while self.running:
            cmd = Command(self.current.get_input())
            if cmd.type is CommandType.INVALID:
                print(choice(INVALID_MSGS))
                continue

            if cmd.type is CommandType.HELP:
                print(HELP_MSG)
            elif cmd.type is CommandType.INTERACT:
                self.current.interact(cmd)
            elif cmd.type is CommandType.INSPECT:
                print(self.current.get_info())
            elif cmd.type in COMMAND_TYPE_TO_DIR:
                room = self.current.side_rooms[COMMAND_TYPE_TO_DIR[cmd.type]]
                if room:
                    self.current.on_leave()
                    self.current = room
                    self.current.on_enter()
