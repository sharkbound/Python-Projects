import re

from itertools import zip_longest
from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from data import Item


def ask_int(prompt, min_=None, max_=None):
    while True:
        v = ask(prompt, int, (ValueError,))

        if min_ is not None and v < min_:
            print('number cannot be less than', min_)
            continue

        if max_ is not None and v > max_:
            print('number cannot be greater than', max_)
            continue

        return v


def ask_float(prompt, min_=None, max_=None):
    while True:
        v = ask(prompt, float, (ValueError,))

        if min_ is not None and v < min_:
            print('number cannot be less than', min_)
            continue

        if max_ is not None and v > max_:
            print('number cannot be greater than', max_)
            continue

        return v


def ask(prompt, func=None, errors=(), options=()):
    while True:
        try:
            v = input(prompt)

            if func:
                v = func(v)

            if options and v not in options:
                print(f'invalid option: {v}\nvalid options: {options}\n')
                continue

            return v

        except errors:
            continue


def str_to_args(cmd):
    return [s.strip(' \'""') for s in re.findall(r'''".*"|'.*'|[^ ]+''', cmd)]


def chunk(items, size, filler=None):
    return zip_longest(*[iter(items)] * size, fillvalue=filler)


def items_to_dict(items) -> 'Dict[str, Item]':
    return {i.name: i for i in items}


def truncate(s: str, length: int):
    return (s[:length - 3] + '...') if len(s) > length else s
