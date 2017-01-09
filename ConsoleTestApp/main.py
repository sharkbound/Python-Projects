from src.timing import Timer
from colorama import Fore, Back
from functools import lru_cache
from collections import namedtuple
from src.logger import *

import timeit, time, struct


@lru_cache(1000)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def main():
    f = 5
    print(f'The factorial of {f} is {factorial(f)}')


if __name__ == '__main__':
    main()
