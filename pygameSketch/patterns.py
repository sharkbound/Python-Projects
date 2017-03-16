from random import randint

min_r = -100
max_r = 100


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


patterns = [
    [
        (30, 0), (0, 30), (-30, 0), (0, -30)
    ],
    [
        pair for pair in create_symmetrical_pairs(start_range=50, stop_range=100, remainder_check_num=10)
        ],
    [
        pair for pair in create_symmetrical_pairs(start_range=50, stop_range=None, remainder_check_num=10)
        ]
]
