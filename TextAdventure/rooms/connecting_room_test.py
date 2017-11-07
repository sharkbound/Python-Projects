from src.room import Room


class ConnectedRoom(Room):
    def __init__(self, src):
        super().__init__('ConnectedRoom', [], left=src)

    def get_info(self):
        return 'info...'

    def on_enter(self):
        print('connected room entered')

    def on_leave(self):
        print('connected room left')