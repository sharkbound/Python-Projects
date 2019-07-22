class lazy_property:
    def __init__(self, getter):
        self.getter = getter
        self._value = None

    def __get__(self, instance, owner):
        if self._value is None:
            self._value = self.getter(instance)
        return self._value
