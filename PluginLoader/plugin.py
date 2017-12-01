class Plugin:
    def __init__(self, name, commands):
        self.commands = commands
        self.name = name

    def loaded(self):
        pass

    def unloaded(self):
        pass