class Event:
    def __init__(self, *subs):
        self.subscribers = list(subs)

    def __iadd__(self, func):
        self.subscribers.append(func)

    def __isub__(self, func):
        if func in self:
            self.subscribers.remove(func)

    def trigger(self, *args, **kwargs):
        for sub in self:
            sub(*args, **kwargs)

    def __call__(self, func):
        self.__iadd__(func)

    def __iter__(self):
        yield from self.subscribers