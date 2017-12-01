from plugin import Plugin

class TestPlugin(Plugin):
    def __init__(self):
        super().__init__('TestPlugin2', [])

    def loaded(self):
        print(self.name, 'has loaded')

    def unloaded(self):
        print(self.name, 'has unloaded')


a = 1