from textadventure.enums import CommandType
from shlex import split

dir_dict = {
    'forward': CommandType.FORWARD,
    'back': CommandType.BACK,
    'left': CommandType.LEFT,
    'right': CommandType.RIGHT
}


class Command:
    def __init__(self, cmd):
        parts = [x.lower() for x in split(cmd)]
        if parts[0] == 'look' and len(parts) == 2:
            self.type = CommandType.LOOK
            self.object_name = parts[1]
        elif parts[0] == 'look' and len(parts) == 1:
            self.type = CommandType.LOOK
        elif parts[0] == 'interact' and len(parts) == 2:
            self.type = CommandType.INTERACT
            self.object_name = parts[1]
        elif parts[0] == 'interact' and len(parts) == 1:
            self.type = CommandType.LIST_INTERACTABLES
        elif parts[0] in ('?', 'help'):
            self.type = CommandType.HELP
        elif parts[0] in dir_dict:
            self.type = dir_dict[parts[0]]
        else:
            self.type = CommandType.INVALID

        if not hasattr(self, 'object_name'):
            self.object_name = None

    def __repr__(self):
        return f'<Command {self.type}: {self.object_name}>'
