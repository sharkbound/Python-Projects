with open('../data.txt') as f:
    lines = [[int(x) for x in line.split()] for line in f]


def checksum(lines):
    def get_result(line):
        print(line)
        for x in line:
            for y in line:
                if x != y and not x % y:
                    return x // y
        return 0

    return sum(map(get_result, lines))


print(checksum(lines))
