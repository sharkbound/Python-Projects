from random import randint
from statistics import mean
from typing import Iterable


class Query:
    def __init__(self, items):
        self.items = iter(items)

    @property
    def as_list(self):
        return list(self.items)

    @property
    def as_tuple(self):
        return tuple(self.items)

    @property
    def as_set(self):
        return set(self)

    def where(self, predicate):
        return Query(x for x in self.items if predicate(x))

    def select(self, func):
        return Query(map(func, self))

    def map(self, func):
        return self.select(func)

    def orderby(self, func=None, reverse=False):
        return Query(sorted(self, key=func, reverse=reverse))

    def average(self):
        return mean(self.as_tuple)

    def mean(self):
        return self.average()

    def first(self, func=None, default=None):
        for x in self:
            if func and func(x):
                return x
            elif not func:
                return x
        return default

    def last(self, func=None, default=None):
        return self.reverse().first(func, default)

    def at(self, index, default=None):
        for i, v in enumerate(self):
            if i == index:
                return v
        return default

    def flatten(self):
        return Query(self.__flatten(self))

    def __flatten(self, x):
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for item in x:
                yield from self.__flatten(item)
        else:
            yield x

    def reverse(self):
        return Query(reversed(self))

    def any(self, predicate=None):
        return any(self) if not predicate else any(map(predicate, self))

    def all(self, predicate=None):
        return all(self) if not predicate else all(map(predicate, self))

    def oftype(self, target_type, include_subclasses=False):
        return self.where(lambda x: isinstance(x, target_type) if include_subclasses else type(x) == target_type)

    def distinct(self):
        return Query(self.as_set)

    def types(self):
        return self.map(lambda x: type(x))

    def __contains__(self, item):
        item_type = type(item)
        return self.any(lambda x: type(x) is item_type and x == item)

    def __reversed__(self):
        return Query(reversed(self.as_tuple))

    def __getitem__(self, item):
        return self.at(item)

    def __iter__(self):
        yield from self.items

    def __str__(self):
        return ', '.join(map(str, self))