from collections import defaultdict
from dataclasses import dataclass
from typing import List


def ask_ints():
    while True:
        v = input('\nenter numbers separated by spaces\n>>> ')
        try:
            return list(map(int, v.split()))
        except ValueError:
            pass


if __name__ == '__main__':
    while True:
        ints = ask_ints()
        for i in range(2, min(ints) + 1):
            if all(not n % i for n in ints):
                pairs = ', '.join(f'{n}={n // i}' for n in ints)
                print(f'{i} -> {pairs}')
