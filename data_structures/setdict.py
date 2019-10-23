from itertools import chain


class setdict(dict):
    def __or__(self, other: dict):
        return self.__class__(chain(self.items(), other.items()))

    def __ior__(self, other: dict):
        for key, value in other.items():
            self[key] = value
        return self

    def __and__(self, other: dict):
        return setdict(pair for pair in self.items() if pair[0] in other)

    def __iand__(self, other: dict):
        for key in tuple(self):
            if key not in other:
                del self[key]
        return self

    def __xor__(self, other: dict):
        return setdict(pair for pair in chain(self.items(), other.items()) if (pair[0] in self) ^ (pair[0] in other))

    def __ixor__(self, other: dict):
        for key in chain(tuple(self), other):
            if not (key in self) ^ (key in other):
                del self[key]
        return self
