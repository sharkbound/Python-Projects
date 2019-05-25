from inspect import isclass


def auto_repr(cls=None, include_private=True):
    def _repr(self):
        return ''.join((
            '<',
            self.__class__.__name__,
            ' ',
            ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items() if
                      include_private or not k[0] == '_'),
            '>',
        ))

    if cls is not None and isclass(cls):
        cls.__repr__ = _repr
        return cls

    def wrapper(cls):
        cls.__repr__ = _repr
        return cls

    return wrapper


@auto_repr(include_private=False)
class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._x = x
        self._y = y
        self.__secret = 'SHHH, dont tell anyone i am here!'


print(Test(1, -1))
