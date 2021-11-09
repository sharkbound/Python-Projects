from typing import Hashable


class Object:
    _cache = {}

    def __new__(cls, value):
        if not isinstance(value, Hashable):
            return super().__new__(cls)

        if value not in cls._cache:
            print(f'new instance for value: {value}')
            cls._cache[value] = super().__new__(cls)

        return cls._cache[value]

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'<{self.__class__.__name__} value={self.value}>'


o1 = Object(1)
o2 = Object(1)
o3 = Object(2)

o1.value += 1

print(o1, o2, o3)
