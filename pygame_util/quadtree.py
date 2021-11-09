from operator import attrgetter
from random import randrange

import numpy as np
from pygame import Rect, Color
from .colors_presets import white, green, blue
from .helpers import render_rect, draw_circle
from typing import List


class QuadTree_OLD:
    def __init__(self, capacity, rect: Rect, center_pos_getter_func=None):
        self.center_pos_getter_func = center_pos_getter_func or (lambda x: x.center)
        self.capacity = capacity
        self.rect = rect
        self.points = []
        self.divided = False
        self.top_left: QuadTree_OLD = None
        self.top_right: QuadTree_OLD = None
        self.bottom_left: QuadTree_OLD = None
        self.bottom_right: QuadTree_OLD = None
        self.children: List[QuadTree_OLD] = []
        # print('init')

    @property
    def all_points(self):
        yield from self.points
        yield from (tree.all_points for tree in self.children)

    @property
    def count(self):
        return len(self.points) + sum(tree.count for tree in self.children)

    def insert(self, rect):
        if len(self.points) >= self.capacity:
            self.subdivide()
            return self.top_left.insert(rect) or self.top_right.insert(rect) or self.bottom_right.insert(
                rect) or self.bottom_left.insert(rect)
        elif self.rect.contains(rect):
            self.points.append(rect)
            return True

        return False

    def subdivide(self):
        if self.divided:
            return

        w, h = self.rect.width / 2, self.rect.height / 2
        self.top_left = QuadTree_OLD(self.capacity, Rect(self.rect.topleft, (w, h)), self.center_pos_getter_func)
        self.top_right = QuadTree_OLD(self.capacity, Rect(self.rect.midtop, (w, h)), self.center_pos_getter_func)
        self.bottom_left = QuadTree_OLD(self.capacity, Rect(self.rect.midleft, (w, h)), self.center_pos_getter_func)
        self.bottom_right = QuadTree_OLD(self.capacity, Rect(self.rect.center, (w, h)), self.center_pos_getter_func)

        self.children.extend((self.top_left, self.top_right, self.bottom_left, self.bottom_right))
        self.divided = True

    def query(self, rect: Rect):
        if not self.rect.colliderect(rect):
            return

        yield from (r for r in self.points if rect.contains(r))
        yield from (r for tree in self.children for r in tree.query(rect))

    def draw(self, grid=True, points=True):
        if not grid and not points:
            return

        for tree in self.children:
            tree.draw(grid, points)

        if grid:
            render_rect(white if not self.count else green, self.rect, 2)

        if points:
            for p in self.points:
                draw_circle(blue, self.center_pos_getter_func(p), 1)


class QuadTree:
    def __init__(self, items, rect: Rect = None, capacity=5, depth=8, color=None):
        self.capacity = capacity
        self.color = color or (randrange(255), randrange(255), randrange(255))

        if rect is not None:
            self.rect = rect
        else:
            self.rect = items[0].rect.unionall([item.rect for item in items[1:]])

        self.depth = depth
        if depth <= 0 or len(items) <= capacity:
            self.items = items
            return

        nw = []
        ne = []
        sw = []
        se = []

        nw_r = Rect(self.rect.topleft, (self.rect.w / 2, self.rect.h / 2))
        ne_r = Rect(self.rect.midtop, (self.rect.w / 2, self.rect.h / 2))
        sw_r = Rect(self.rect.midleft, (self.rect.w / 2, self.rect.h / 2))
        se_r = Rect(self.rect.center, (self.rect.w / 2, self.rect.h / 2))

        cx, cy = self.rect.center
        for item in items:
            r = item.rect
            x = item.rect.center[0]
            y = item.rect.center[1]

            if x <= cx and y <= cy:
                nw.append(item)
            elif x >= cx and y <= cy:
                ne.append(item)
            elif x <= cx and y >= cy:
                sw.append(item)
            elif x >= cx and y >= cy:
                se.append(item)

        self.items = tuple()
        self.nw = QuadTree(nw, nw_r, color=color)
        self.ne = QuadTree(ne, ne_r, color=color)
        self.sw = QuadTree(sw, sw_r, color=color)
        self.se = QuadTree(se, se_r, color=color)

    # def query_rect(self, rect: Rect):
    #     if self.items:
    #         yield from rect.collidelistall([i.rect for i in self.items])
    #     elif hasattr(self, 'ne'):
    #         yield from self.ne.query_rect(rect)
    #         yield from self.nw.query_rect(rect)
    #         yield from self.se.query_rect(rect)
    #         yield from self.sw.query_rect(rect)

    def query(self, rect: Rect):
        if not self.rect.colliderect(rect):
            return

        if self.items:
            yield from (i for i in self.items if rect.contains(i.rect))
        elif hasattr(self, 'ne'):
            yield from self.ne.query(rect)
            yield from self.nw.query(rect)
            yield from self.se.query(rect)
            yield from self.sw.query(rect)

    def draw(self, grid=True, points=True, draw_grid_always=False):
        if draw_grid_always:
            if self.items:
                render_rect((0, 150, 0), self.rect, 1)
            else:
                render_rect(white, self.rect, 1)

        if self.items:
            if points:
                for item in self.items:
                    render_rect(self.color, item.rect, 1)
        elif hasattr(self, 'ne'):
            self.ne.draw(grid, points, draw_grid_always)
            self.nw.draw(grid, points, draw_grid_always)
            self.se.draw(grid, points, draw_grid_always)
            self.sw.draw(grid, points, draw_grid_always)

    def __str__(self):
        return f'<SELF {self.items}, NW {getattr(self, "nw.items", None)}, NE {getattr(self, "ne.items", None)},' \
               f' SW {getattr(self, "sw.items", None)}, SE {getattr(self, "se.items", None)}>'

    # def draw(self, grid=True, points=True):
    #     if not grid and not points:
    #         return
    #
    #     if self.
    #     for tree in self.children:
    #         tree.draw(grid, points)
    #
    #     if grid:
    #         render_rect(white if not self.count else green, self.rect, 2)
    #
    #     if points:
    #         for p in self.points:
    #             draw_circle(blue, self.center_pos_getter_func(p), 1)
