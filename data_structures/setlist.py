from collections import defaultdict, UserList


class setlist(UserList):
    _ADD, _REMOVE, _INC_COUNT = range(3)

    def __init__(self, iterable=()):
        super().__init__(iterable)
        self._seen = set()
        self._counts = defaultdict(lambda: 0)

    def _update(self, obj, mode=_ADD):
        if mode == self._REMOVE:
            super().remove(obj)
            self._counts[obj] -= 1
            if not self._counts[obj]:
                del self._counts[obj]
            self._seen.remove(obj)

        elif mode == self._ADD:
            super().append(obj)
            self._update(obj, self._INC_COUNT)

        elif mode == self._INC_COUNT:
            self._counts[obj] += 1
            self._seen.add(obj)

    def append(self, obj):
        self._update(obj, self._ADD)

    def extend(self, iterable):
        for item in iterable:
            self._update(item, self._ADD)

    def remove(self, obj):
        self._update(obj, self._REMOVE)

    def count(self, obj):
        return self._counts[obj]
