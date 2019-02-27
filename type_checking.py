from typing import Sized, Callable


class Checked:
    def __init__(self, *handlers):
        self.handlers = handlers

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        for handler in self:
            handler(value)
        instance.__dict__[self.name] = value

    def __iter__(self):
        for handler in self.handlers:
            if isinstance(handler, Checked):
                yield from handler
            elif callable(handler) and handler.__code__.co_argcount == 1:
                yield handler
            else:
                raise TypeError(f'invalid handler type {type(handler)}, expected {Checked} or {Callable}')


def require_type(value, *types, message='Got type {type}, expected {types}'):
    if not isinstance(value, types):
        raise TypeError(message.format(type=type(value), types=types))


def require(passed, message):
    if not passed:
        raise ValueError(message)


def str_(value):
    require_type(value, str)


def int_(value):
    require_type(value, int)


def float_(value):
    require_type(value, float)


def maxed(maxlen):
    def _sized(value):
        require_type(value, Sized)
        if len(value) > maxlen:
            raise ValueError(f'length cannot exceed {maxlen}')

    return _sized


def ranged_number(min_, max_):
    def _range_number(value):
        require(min_ <= value <= max_, f'number must be between {min_} and {max_}')

    return _range_number


def ranged_len(min_, max_):
    def _ranged_len(value):
        require(min_ <= len(value) <= max_, f'len() must be between {min_} and {max_}')

    return _ranged_len


def create_type(*handlers):
    def _create():
        return Checked(*handlers)

    return _create


def sized(value):
    require_type(value, Sized)


String = create_type(str_)
Int = create_type(int_)
Float = create_type(float_)
Number = create_type(int_, float_)

SizedString = lambda maxlen: create_type(String(), maxed(maxlen))()
RangedNumber = lambda min_, max_: create_type(Number(), ranged_number(min_, max_))()
RangedLength = lambda min_, max_: create_type(sized, ranged_len(min_, max_))()


class C:
    i = RangedLength(1, 20)

    def __init__(self, i):
        self.i = i
