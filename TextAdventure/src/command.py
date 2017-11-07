from enums.command_type import CommandType
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
        if parts[0] == 'inspect' and len(parts) == 2:
            self.type = CommandType.INSPECT
            self.object_name = parts[1]
        elif parts[0] == 'interact' and len(parts) == 2:
            self.type = CommandType.INTERACT
            self.object_name = parts[1]
        elif parts[0] == 'help':
            self.type = CommandType.HELP
        elif parts[0] in dir_dict:
            self.type = dir_dict[parts[0]]
        else:
            self.type = CommandType.INVALID

        if not hasattr(self, 'object_name'):
            self.object_name = None

    def __str__(self):
        return f'{self.type}: {self.object_name}'
