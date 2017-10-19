from random import randrange, randint
from statistics import mean
from typing import Iterable
from itertools import chain, tee


class Query:
    def __init__(self, items):
        self.items = iter(items)
        self.count = sum(1 for _ in self)

    @property
    def as_list(self):
        """get all the current values as a list"""
        return list(self)

    @property
    def as_tuple(self):
        """get all the current values as a tuple"""
        return tuple(self)

    @property
    def as_set(self):
        """get all the current values as a set"""
        return set(self)

    def iteritems(self):
        self.items, ret = tee(self.items)
        return ret

    def where(self, predicate):
        """filters values by a function"""
        return Query(x for x in self if predicate(x))

    def select(self, func):
        """applies a function to all values"""
        return Query(map(func, self))

    def map(self, func):
        """same as select, applies a function to all values"""
        return self.select(func)

    def orderby(self, func=None, reverse=False):
        """orders values according to a func, or by raw values if func is None"""
        return Query(sorted(self, key=func, reverse=reverse))

    def average(self):
        """returns a the average of all values"""
        return mean(self.as_tuple)

    def mean(self):
        """returns a mean of all values (same as average)"""
        return self.average()

    def first(self, func=None, default=None):
        """returns first item that ether meets the condition or first item in value if func in None"""
        for x in self:
            if func and func(x):
                return x
            elif not func:
                return x
        return default

    def last(self, func=None, default=None):
        """returns last item that ether meets the condition or last item in value if func in None"""
        return self.reverse().first(func, default)

    def at(self, index, default=None):
        """gets a value at specified index, returns default value of not found"""
        for i, v in enumerate(self):
            if i == index:
                return v
        return default

    def flatten(self):
        """flattens current values to all be in a single query"""
        return Query(self.__flatten(self))

    def __flatten(self, x):
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for item in x:
                yield from self.__flatten(item)
        else:
            yield x

    def reverse(self):
        """returns a reversed query"""
        return Query(reversed(self))

    def any(self, predicate=None):
        """returns true if any values evaluate to true else false"""
        return any(self) if not predicate else any(map(predicate, self))

    def all(self, predicate=None):
        """returns true if all the values evaluate to true else false"""
        return all(self) if not predicate else all(map(predicate, self))

    def oftype(self, target_type, include_subclasses=False):
        """returns a query with all values of the target_type"""
        return self.where(lambda x: isinstance(x, target_type) if include_subclasses else type(x) == target_type)

    def distinct(self):
        """returns a query with no repeated values"""
        return Query(self.as_set)

    def types(self):
        """returns a query with all the type of the current items"""
        return self.map(lambda x: type(x))

    def max(self, func=None):
        """get the max value from all current items, filters by function if func is not None"""
        if func:
            return max(map(func, self))
        return max(self)

    def min(self, func=None):
        """get the min value from all current items, filters by function if func is not None"""
        if func:
            return min(map(func, self))
        return min(self)

    def add(self, *values):
        return Query(chain(self, *values))

    def shuffle(self):
        return Query(self.orderby(lambda x: randrange(self.count+1)))

    def __contains__(self, item):
        item_type = type(item)
        return self.any(lambda x: type(x) is item_type and x == item)

    def __reversed__(self):
        return Query(reversed(self.as_tuple))

    def __getitem__(self, item):
        return self.at(item)

    def __iter__(self):
        return self.iteritems()

    def __str__(self):
        return ', '.join(map(str, self))


