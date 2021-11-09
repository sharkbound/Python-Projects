import re
from pprint import pprint
from random import choice


class Node:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = int(weight)
        self._children = tuple(children)

    @property
    def children(self):
        return tuple(map(nodes.get, self._children))

    @property
    def isparent(self):
        return bool(self.children)

    def __iter__(self):
        yield from self.children

    def __str__(self):
        return f'<Node {self.name}:{self.weight}:{self.isparent}>'

    __repr__ = __str__

    @classmethod
    def from_str(cls, string):
        match = re.match(r'(\w+) \((\d+)\)(?: -> (.*))?', string)
        return cls(match[1], match[2], (s.strip() for s in match[3].split(',')) if match[3] else ())


def get_parent(node):
    for n in nodes.values():
        if node in n.children:
            return n


def get_root():
    last = choice(tuple(nodes.values()))
    parent = last
    while parent is not None:
        last = parent
        parent = get_parent(parent)
    return last


file_name = 'data.txt'
with open(file_name) as f:
    nodes = {n.name: n for n in map(Node.from_str, f)}


def part1():
    node = get_root()
    while node.isparent:
        node = node.children[-1]
    print(node)


if __name__ == '__main__':
    part1()
