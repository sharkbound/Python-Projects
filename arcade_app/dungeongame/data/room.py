from .interactables import Interactables


class Room:
    def __init__(self, key):
        self.key = key
        self.interactables = Interactables()
