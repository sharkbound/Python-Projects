from functools import reduce
from random import randrange
from statistics import variance
from typing import Iterable
from itertools import chain, tee


class Query:
    def __init__(self, items):
        self.items = iter(items)

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

    def count(self, predicate=None):
        if predicate:
            return sum(1 for x in self if predicate(x))
        return sum(1 for _ in self)

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

    def average(self, func=None):
        """returns a the average of all values"""
        return self.sum(func) / self.count()

    def first(self, predicate=None, default=None):
        """returns first item that ether meets the condition or first item in value if func in None"""
        for x in self:
            if predicate and predicate(x) or not predicate:
                return x
        return default

    def last(self, predicate=None, default=None):
        """returns last item that ether meets the condition or last item in value if func in None"""
        return self.reverse().first(predicate, default)

    def at(self, index, default=None):
        """gets a value at specified index, returns default value if not found"""
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
        """returns a query with all the types of the current items"""
        return self.map(lambda x: type(x))

    def max(self, func=None):
        """get the max value from all current items, filters by function if func is not None"""
        if func:
            return max(map(func, self))
        return max(self)

    def min(self, func=None):
        """get the min value from all current items, filters byf unction if func is not None"""
        if func:
            return min(map(func, self))
        return min(self)

    def add(self, *values):
        """adds other iterables to the current items"""
        return Query(chain(self, *values))

    def shuffle(self, func=None):
        """randomly orders items, using func if provided"""
        count = self.count() + 1
        if not func:
            func = lambda x: randrange(count)
        return Query(self.orderby(func))

    def sum(self, func=None):
        """returns the sum of all values"""
        if func:
            return sum(map(func, self))
        return sum(self)

    # def aggregate(self, func, start_value=None):
    #     """returns the result of the function with the result of the last call as the first parameter, and the next item the second"""
    #     if start_value is not None:
    #         return reduce(func, self, start_value)
    #     return reduce(func, self, self.at(0))

    def filter_nones(self):
        return Query(self.where(lambda x: x is not None))

    def variance(self, xbar=None):
        return variance(self, xbar)

    def similar(self, items):
        """returns a Query with all items that are the same with the same index between the 2 iterables"""
        def _similar():
            for v1, v2 in zip(self, items):
                if v1 == v2:
                    yield v1
        return Query(_similar())

    def different(self, items):
        """returns a query with all items that are different with the same index between the 2 iterables"""
        def _diff():
            for v1, v2 in zip(self, items):
                if v1 != v2:
                    yield (v1, v2)
        return Query(_diff())

    def __len__(self):
        return self.count()

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
        return ', '.join(self.map(str))
