def index_to_xy(index, rows, cols):
    return index % rows, index // cols


def xy_to_index(x, y, rows, cols):
    return y * rows + x


if __name__ == '__main__':
    index = 21
    assert index_to_xy(21, 10, 10) == (1, 2)
    assert xy_to_index(1, 2, 10, 10) == 21
