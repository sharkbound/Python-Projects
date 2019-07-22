from typing import Mapping

_NO_DEFAULT = object()


class Obj:
    @classmethod
    def from_map(cls, mapping: Mapping):
        o = cls()
        for key, value in mapping.items():
            setattr(o, key, value)
        return o

    def __getattr__(self, item):
        return self.__dict__[item]

    def __str__(self):
        pairs = ' '.join(f'{key}={value!r}' for key, value in self.__dict__.items() if not key.startswith('_'))
        return f'<{self.__class__.__name__} {pairs}>'


def get_all_keys(mapping: Mapping, *keys, default=_NO_DEFAULT, as_obj=False):
    if default is not _NO_DEFAULT:
        gen = (mapping.get(key, default) for key in keys)
    else:
        gen = (mapping[key] for key in keys)

    if as_obj:
        obj = Obj()
        for key, value in zip(keys, gen):
            setattr(obj, key, value)
        return obj
    return tuple(gen)


def to_obj(mapping: Mapping) -> Obj:
    return Obj.from_map(mapping)
