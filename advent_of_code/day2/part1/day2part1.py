with open('../data.txt') as f:
    lines = [[int(x) for x in line.split()] for line in f]

def checksum():
    return sum([max(l) - min(l) for l in lines])

print(checksum())
