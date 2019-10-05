from enum import IntFlag
from random import choice, random
from time import sleep


def chance(percent):
    return random() < percent


def rand_char():
    return choice('█ ')


WALL, AIR, FLOOR, RANDOM = IntFlag('TileType', 'WALL AIR FLOOR RANDOM')

NEXT_TILETYPE = {
    WALL: lambda: WALL if chance(.8) else AIR,
    AIR: lambda: AIR if chance(.4) else RANDOM,
    FLOOR: lambda: RANDOM,
    RANDOM: lambda: choice((WALL, AIR, FLOOR))
}

TILETYPE_TO_CHARACTER = {
    WALL: lambda: '█',
    AIR: lambda: ' ',
    FLOOR: lambda: '_',
    RANDOM: lambda: rand_char(),
}


def run(row, *, delay=.5):
    while True:
        row = [NEXT_TILETYPE[item]() for item in row]

        print(*(TILETYPE_TO_CHARACTER[item]() for item in row), sep='')
        sleep(delay)


run([WALL] * 150, delay=.05)
