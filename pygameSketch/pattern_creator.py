from random import randint

def create_symmetrical_pairs(start_range, stop_range=None, remainder_check_num=20):
    if stop_range != None:
        for num in range(start_range, stop_range):
            if num % remainder_check_num == 0:
                yield (num, -num)
                yield (-num, num)
    else:
        for num in range(start_range):
            if num % remainder_check_num == 0:
                yield (num, -num)
                yield (-num, num)


def make_pair(numbers):
    for n in numbers:
        yield (n, -n)
        yield (-n, n)

class Pattern:
    def __init__(self, points, size = (2, 2)):
        self.points = points
        self.size  = size