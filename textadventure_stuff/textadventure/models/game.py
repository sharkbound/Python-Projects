from textadventure.enums import CommandType, Direction
from rooms.starting_room import StartingRoom
from .command import Command
from random import choice
from textadventure.util import *

HELP_MSG = """Commands: 
look -> tells you about your current room
inspect {object_name} -> inspects a object
interact {object_name} -> interacts with a object, doing just `interact` will show interactive objects
help -> show this menu"""

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
            entered_input = self.current.input.strip()
            if not entered_input:
                continue

            cmd = Command(entered_input)
            if cmd.type is CommandType.INVALID:
                print(choice(INVALID_MSGS))
                continue

            if cmd.type is CommandType.HELP:
                print(HELP_MSG)
            elif cmd.type is CommandType.INTERACT:
                self.current.interact(cmd)
            elif cmd.type is CommandType.LOOK:
                print(self.current.info)
            elif cmd.type is CommandType.LIST_INTERACTABLES:
                print(self.current.interactables_str)
            elif cmd.type in COMMAND_TYPE_TO_DIR:
                room = get_room(self.current.side_rooms[COMMAND_TYPE_TO_DIR[cmd.type]])
                if room is not None:
                    self.current.on_leave()
                    self.current = room
                    self.current.on_enter()
