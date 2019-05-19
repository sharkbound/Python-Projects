class Maybe:
    def __init__(self, value=None, copy=False):
        self._copy = copy
        self._value = value

    @property
    def value_or_none(self):
        return self._value if self else None

    @property
    def value(self):
        return self._value

    def _get_value(self, value):
        if self._copy:
            return self.__class__(value)
        self._value = value
        return self

    def map_or_default(self, func, default):
        return self._get_value(default if not self else func(self._value))

    def map(self, func):
        return self & func

    def filter(self, func):
        if not self or not func(self._value):
            self._value = None
            return self
        return self

    def filter_or_else(self, func, default):
        if not self or not func(self):
            return self._get_value(default)
        return self

    def default(self, default):
        return self._value if self else default

    __and__ = filter
    __lshift__ = filter

    def __rshift__(self, func):
        if not self:
            return self
        return self._get_value(func(self._value))

    def __bool__(self):
        return self._value is not None

    def __or__(self, default):
        return self._value if self else default

    def __repr__(self):
        return f'<{"(Mutable)" if not self._copy else ""}Maybe {self._value!r}>'


def try_parse(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None
