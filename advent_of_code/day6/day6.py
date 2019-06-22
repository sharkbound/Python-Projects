def read_data():
    with open('data.txt') as f:
        return [int(x) for x in f.readline().split()]


class Data:
    def __init__(self):
        self.values = read_data()
        self.index = 0
        self.steps = 0

    copy = property(lambda self: tuple(self.values))
    value = property(lambda self: self[self.cur_index])
    max_value_index = property(lambda self: self.values.index(max(self)))

    def next_index(self):
        self.index = (self.index + 1) % len(self.values)
        return self.index

    def distribute(self, amt):
        self[self.index] = 0
        for _ in range(amt):
            self[self.next_index()] += 1

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __iter__(self):
        yield from self.values

    def __str__(self):
        return str(self.values)


def part1():
    data = Data()
    seen_states = set()

    while data.copy not in seen_states:
        data.steps += 1
        seen_states.add(data.copy)
        data.index = data.max_value_index
        data.distribute(data[data.index])

    return data.steps

def part2():
    data = Data()

    for _ in range(2):
        seen_states = set()
        data.steps = 0

        while data.copy not in seen_states:
            data.steps += 1
            seen_states.add(data.copy)
            data.index = data.max_value_index
            data.distribute(data[data.index])

    return data.steps


print(part1())
print(part2())
