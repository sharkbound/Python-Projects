class BitFlagGenerator:
    def __init__(self, initial=1):
        self._check_is_flag(initial)
        self.current = initial

    def _check_is_flag(self, value):
        if not sum(1 for bit in bin(value) if bit == '1') == 1:
            raise ValueError('flag must only have active bit')

    def _gen_next(self):
        current = self.current
        self.current <<= 1
        return current

    def list(self, count=1):
        return list(self[count])

    def tuple(self, count=1):
        return tuple(self[count])

    def generator(self, count=1):
        return self[count]

    def __getitem__(self, count=1):
        yield self._gen_next()
        if count > 1:
            yield from (self._gen_next() for _ in range(count - 1))

    def __next__(self):
        return next(self[1])


f = BitFlagGenerator()
print(*f.generator(4), f.tuple(4))
