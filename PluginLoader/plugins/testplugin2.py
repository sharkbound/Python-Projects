from plugin import Plugin

class TestPlugin2(Plugin):
    def __init__(self):
        super().__init__('TestPlugin', [])

    def loaded(self):
        print(self.name, 'has loaded')

    def unloaded(self):
        print(self.name, 'has unloaded')


class Test2(TestPlugin2, Plugin):
    def __init__(self):
        super().__init__()
        print(super())
