from models.interactable import Interactable


class Lamp(Interactable):
    def __init__(self):
        super().__init__('lamp')
        self.on = False

    def interact(self):
        self.on = not self.on
        print('you turned the lamp on' if self.on else 'you turned the lamp off')