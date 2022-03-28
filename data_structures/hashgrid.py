import abc
from collections import defaultdict
from pprint import pprint
from typing import Any, Hashable

from icecream import ic


def _iter_2d_coords(topleft, bottomright, bucket_size):
    for x in range(min(int(topleft[0]), int(bottomright[0])) // bucket_size, (max(int(topleft[0]), int(bottomright[0])) // bucket_size) + 1):
        for y in range(min(int(topleft[1]), int(bottomright[1])) // bucket_size, (max(int(topleft[1]), int(bottomright[1])) // bucket_size) + 1):
            yield x, y


class HashGrid:
    def __init__(self, bucket_size=200):
        self.bucket_size = bucket_size
        self.contents: defaultdict[Hashable, list] = defaultdict(list)
        self._buckets_for_object: dict[Hashable, list] = defaultdict(list)

    def add(self, obj, bounds):
        for x, y in _iter_2d_coords(bounds[0], bounds[1], self.bucket_size):
            bucket = self.contents[x, y]
            bucket.append(obj)
            self._buckets_for_object[obj].append(bucket)

    def add_all(self, *obj_bound_pairs):
        for obj, bound in obj_bound_pairs:
            self.add(obj, bound)

    def remove(self, obj):
        if obj not in self._buckets_for_object:
            return False
        for bucket in self._buckets_for_object[obj]:
            bucket.remove(obj)
        del self._buckets_for_object[obj]

    def to_bucket_coord(self, point):
        return int(point[0] // self.bucket_size), int(point[1] // self.bucket_size)

    def clear_bounds(self, bounds, filter_func=None):
        for x, y in _iter_2d_coords(bounds[0], bounds[1], self.bucket_size):
            if (coords := (x, y)) in self.contents:
                bucket = self.contents[coords]
                if filter_func is None:
                    bucket.clear()
                    del self.contents[coords]
                else:
                    container = bucket
                    for obj in tuple(filter(filter_func, container)):
                        container.remove(obj)
                        self._buckets_for_object[obj].remove(container)
                    if not container:
                        del self.contents[coords]

    def clear_point(self, point, filter_func=None):
        point = self.to_bucket_coord(point)
        if point not in self.contents:
            return

        bucket = self.contents[point]
        if filter_func is None:
            bucket.clear()
            del self.contents[point]
        else:
            container = bucket
            for obj in tuple(filter(filter_func, container)):
                container.remove(obj)
                self._buckets_for_object[obj].remove(container)
            if not container:
                del self.contents[point]

    def clear(self):
        self.contents.clear()
        self._buckets_for_object.clear()

    def get_objects_for_point(self, point):
        point = self.to_bucket_coord(point)
        if point in self.contents:
            return tuple(self.contents[point])
        return ()

    def get_objects_for_area(self, bounds):
        objects = []
        for point in _iter_2d_coords(bounds[0], bounds[1], self.bucket_size):
            if point in self.contents:
                objects.extend(self.contents[self.to_bucket_coord(point)])
        return set(objects)

    def debug(self):
        print('--------------------------------------------------------')
        print(f'{self.contents=}\n\t{len(self.contents)=}')
        print(f'{self._buckets_for_object=}\n\t{len(self._buckets_for_object)=}')
        print('--------------------------------------------------------')
