class DictAttributeMixin:
    _map_name_ = 'data'

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]
        return self.__dict__[self._map_name_][item]


class DictItemGetterMixin:
    _map_name_ = 'data'

    def __getitem__(self, item):
        if not isinstance(item, tuple):
            return self.__dict__[self._map_name_][item]

        new_err = None

        try:
            value = self.__dict__[self._map_name_][item[0]]
            for k in item[1:]:
                value = value[k]
            return value

        except KeyError as e:
            raise RuntimeError(f'invalid key: {k} for {value!r}') from e

        except IndexError as e:
            raise RuntimeError(f'out of bounds index: {k} for {value!r}') from e


class AttrClass(DictAttributeMixin, DictItemGetterMixin):
    _map_name_ = 'data'

    def __init__(self, **kwargs):
        self.data = kwargs
