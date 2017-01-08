from src.timing import Timer
from colorama import Fore, Back
from functools import lru_cache
from collections import namedtuple

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

    timer = Timer()
    time.sleep(5)
    print(f'{Fore.BLUE}The time after sleeping is: {timer.get_time()}')
    timer.reset()
    time.sleep(3)
    print(f'Time after 3 seconds of sleep: {timer.get_time()}')
    print(f'{Fore.LIGHTRED_EX}Total time: {timer.get_total_time()}')

# equivilant of C# structs in python:

# structtest = namedtuple('structtest', 'f1, f2, f3, f4')
# st = structtest('var1', 'var2', 'var3', 'var4')
# print(Fore.CYAN+st[2])   both work.
# print(Fore.CYAN+st.f3)