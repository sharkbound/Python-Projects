import pattern_creator as pc

# (int, int) is the height and width
pattern_list = [
    pc.Pattern([(0,0)]),
    pc.Pattern([
        (30, 0), (0, 30), (-30, 0), (0, -30)
    ]),

    pc.Pattern(
        [
            pair for pair in pc.create_symmetrical_pairs(start_range=50, remainder_check_num=10)
            ]),

    pc.Pattern([
        (-50, -50), (-30, -50), (-10, -50), (10, -50), (30, -50), (50, -50),  # top line
        (-50, 50), (-30, 50), (-10, 50), (10, 50), (30, 50), (50, 50),  # botton line
        (-50, 50), (-50, 30), (-50, 10), (-50, -10), (-50, -30),  # left line
        (50, 50), (50, 30), (50, 10), (50, -10), (50, -30),  # right line
    ], (2, 2))
]


def get_pattern_at(index):
    if index_in_bounds(index):
        return pattern_list[index]
    return pattern_list[-1]


def index_in_bounds(index):
    if index < len(pattern_list):
        return True
    return False


def get_next_pattern(curr_index):
    if index_in_bounds(curr_index + 1):
        return pattern_list[curr_index + 1]
    else:
        return pattern_list[0]


def init_patterns():
    pass
