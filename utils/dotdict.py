import typing


class DotDict(dict):
    def __getattr__(self, item):
        return self.__getitem__(item)

    def __setattr__(self, key, value):
        self[key] = value

    def _is_mutable_mapping(self, mapping):
        return isinstance(mapping, typing.MutableMapping) and type(mapping) is not type(self)

    def _transform_if_mutable_mapping(self, value):
        if self._is_mutable_mapping(value):
            print(f'_transform_if_mutable_mapping -> {value}')
            return type(self)(value)

        return None

    def _transform_if_mutable_sequence(self, value):
        if isinstance(value, typing.MutableSequence):
            print(f'_transform_if_mutable_sequence -> {value}')
            return [
                self._transform_if_mutable_mapping(subvalue)
                or self._transform_if_mutable_sequence(subvalue)
                or value

                for i, subvalue in enumerate(value)
            ]

        return None

    def __getitem__(self, item):
        value = super().__getitem__(item)

        return (
                self._transform_if_mutable_mapping(value)
                or self._transform_if_mutable_sequence(value)
                or value
        )

    def __missing__(self, key):
        self[key] = self.__class__()
        return self[key]

    def __repr__(self):
        return f'{self.__class__.__name__}({super().__repr__()})'


if __name__ == '__main__':
    dot = DotDict()
    dot.value = {'subvalue': 'value'}
    dot.manylists = [[[[[{'text': 'convert me!', 'sublists2': [[[[[{'eversubber!': 'value!!'}]]]]]}]]]]]
    print(dot.manylists)
