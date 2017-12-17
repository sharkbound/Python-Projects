def get_jumps():
    with open('input.txt') as datafile:
        return [int(s) for s in datafile]


def part1():
    jumps = get_jumps()
    i, l, c = 0, len(jumps), 0
    while 0 <= i < l:
        c += 1
        tmp = i
        i += jumps[i]
        jumps[tmp] += 1
    print('part 1 solution:', c)


def part2():
    jumps = get_jumps()
    i, l, c = 0, len(jumps), 0
    while 0 <= i < l:
        c += 1
        tmp = i
        i += jumps[i]
        jumps[tmp] += -1 if jumps[tmp] >= 3 else 1
    print('part 2 solution:', c)

class c: pass
class d(c): pass
part1()  # 342669
part2()  # 25136209
