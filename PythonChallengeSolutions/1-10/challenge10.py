import itertools


def look_and_say(length):
    table = {
        ("1", "1", "1"): "31",
        ("1", "1"): "21",
        ("1",): "11",
        ("2", "2", "2"): "32",
        ("2", "2"): "22",
        ("2",): "12",
        ("3", "3", "3"): "33",
        ("3", "3"): "23",
        ("3",): "13"
    }

    prec, result = "1", [1]

    for i in range(length - 1):
        prec = "".join(table[tuple(l)] for e, l in itertools.groupby(prec))
        result.append(int(prec))

    return result


# i got stuck on this problem, had to look it up
if __name__ == '__main__':
    print(len(str(look_and_say(31)[30])))
