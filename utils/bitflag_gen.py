class BitFlagGenerator:
    def __init__(self, initial=1):
        self._check_is_flag(initial)
        self.initial = initial
        self.current = initial
        self.flags = []

    def _check_is_flag(self, value):
        if not sum(1 for bit in bin(value) if bit == '1') == 1:
            raise ValueError('flag must only have active bit')

    def _gen_next(self):
        self.flags.append(self.current)
        current = self.current
        self.current <<= 1
        return current

    def list(self, count=1):
        return list(self(count))

    def tuple(self, count=1):
        return tuple(self(count))

    def generator(self, count=1):
        return self(count)

    def reset(self, initial=1):
        self.current = initial
        self.flags.clear()
        return self

    def copy(self):
        new_bit_flag_gen = self.__class__(self.initial)
        new_bit_flag_gen.flags = self.flags.copy()
        return new_bit_flag_gen

    def __getitem__(self, item):
        return self.flags[item]

    def __call__(self, count=1):
        yield self._gen_next()
        if count > 1:
            yield from (self._gen_next() for _ in range(count - 1))

    def __next__(self):
        return next(self(1))


def create_flags(count):
    for i in range(count):
        yield 1 << i
