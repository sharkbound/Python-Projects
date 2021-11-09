from itertools import count


def to_hex(value):
    hex_chars = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    out = []

    while value:
        bits = value & 15
        out.append(hex_chars.get(bits, str(bits)))
        value >>= 4

    return '0x' + ''.join(reversed(out))


def from_hex(value):
    if not value or not isinstance(value, str):
        return 0

    value = value.replace('0x', '')
    hex_chars_to_value = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

    total = 0
    power = 0
    for char in reversed(value):
        num = int(char) if char.isnumeric() else hex_chars_to_value[char.lower()]
        total += num * (16 ** power)
        power += 1

    return total
