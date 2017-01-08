from src.timing import Timer
from colorama import Fore, Back
from functools import lru_cache

import math, bettertimeit
import timeit, time


@lru_cache(1000)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def fact():
    print(f'Factorial of 5 {factorial(5)}')


def main():
    f = 5
    print(f'The factorial of {f} is {factorial(f)}')


if __name__ == '__main__':
    main()
    # t = Timer()
    # t.start_time()
    # time.sleep(5)
    # t.print()
    #
    # t2 = Timer()
    # t2.time_exec(lambda: (
    #     print(1),
    #     time.sleep(3),
    #     print(2)
    # ), 2)

    # t2.time_exec(lambda: time.sleep(2), 2)
    # print(f'{Fore.GREEN}GREEN{Fore.RED}RED{Fore.LIGHTYELLOW_EX}YELLOW')
    # value = timeit.timeit(stmt=main, number=1)
    # print(f'value: {value}')
