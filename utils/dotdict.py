import typing


class DotDict(dict):
    def __getattr__(self, item):
        return self.__getitem__(item)

    def __setattr__(self, key, value):
        self[key] = value

    def _is_mutable_mapping(self, mapping):
        return isinstance(mapping, typing.MutableMapping) and type(mapping) is not type(self)

    def __getitem__(self, item):
        value = super().__getitem__(item)

        if self._is_mutable_mapping(value):
            value = DotDict(value)
            self[item] = value

            for key, subvalue in tuple(value.items()):
                if self._is_mutable_mapping(subvalue):
                    value[key] = type(self)(subvalue)

        elif isinstance(value, typing.MutableSequence):
            for index, item in enumerate(value):
                if self._is_mutable_mapping(item):
                    value[index] = DotDict(item)

        return value

    def __missing__(self, key):
        self[key] = self.__class__()
        return self[key]

    def __repr__(self):
        return f'{self.__class__.__name__}({super().__repr__()})'


if __name__ == '__main__':
    dot = DotDict()
    dot.value = {'subvalue': 'value'}
    dot.list = [{'test': 'value'}]
    print(dot)
    print(dot.value)
    print(dot)
    print(dot.list)
    print(dot)
