from collections import UserDict


class SafeDict(UserDict):
    def __init__(self, mapping):
        super().__init__(mapping)
        self.mapping = mapping
        self.default = None

    def get(self, keys, default=None):
        self.default = default
        v = super().get(keys, default=default)
        self.default = None
        return v

    def __getitem__(self, items):
        try:
            if not isinstance(items, tuple):
                return self.data[items]

            v = self.data[items[0]]
            for item in items[1:]:
                v = v[item]
        except (KeyError, TypeError):
            v = self.default
        return v


def safe_get(mapping, *items, default=None):
    try:
        v = mapping[items[0]]
        for item in items[1:]:
            v = v[item]
    except (KeyError, TypeError):
        v = default
    return v
