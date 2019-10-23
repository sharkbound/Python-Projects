class dynamic_property:
    def __init__(self, getter):
        self.get = getter
        self.set = None

    def __get__(self, instance, owner):
        return self.get(instance or owner, instance is not None, owner is not None)

    def __set__(self, instance, value):
        self.set(instance, value)


class C:
    def __init__(self):
        self._value = -1

    @dynamic_property
    def value(self, inst, cls):
        if inst:
            return self._value
        else:
            return 'Nope'


print(C().value)
print(C.value)
input()
