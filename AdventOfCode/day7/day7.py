import re

class Node:
    def __init__(self, name, weight, subprograms):
        self.name = name
        self.weight = int(weight)
        self.subprograms = subprograms

    @property
    def isparent(self):
        return bool(self.subprograms)

    def __str__(self):
        return f'<Node {self.name}:{self.weight}:{self.isparent}>'
from operator import itemgetter


def readdata():
    with open('data.txt') as f:
        yield from f


def process(lines):
    for l in lines:
        parts = tuple(re.split('->', l.rstrip()))
        subprograms = tuple()

        if len(parts) == 2:
            subprograms = tuple(s.strip() for s in parts[1].split(','))

        name, weight = parts[0].split()
        yield Node(name, weight[1:-1], subprograms)


def getdata(): return tuple(process(readdata()))
def iterdata(): return process(readdata())

def part1():
    print(*getdata())

part1()
