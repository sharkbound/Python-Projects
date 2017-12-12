from collections import Counter

with open('input.txt') as test_input_file:
    passcodes = [s.strip().split() for s in test_input_file]

valid_passcodes_part_1 = lambda: [pc for pc in passcodes if len(set(pc)) == len(pc)]


def valid_passcodes_part_2():
    valid_count = 0
    for pc in valid_passcodes_part_1():
        isvalid = True
        for w in pc:
            c = Counter(w)
            if any(Counter(x) == c for x in pc if x != w):
                isvalid = False
                break

        valid_count += int(isvalid)
    return valid_count

print(len(valid_passcodes_part_1()))
print(valid_passcodes_part_2())


