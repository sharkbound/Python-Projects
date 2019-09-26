def to_hex(value):
    hex_chars = {10: 'a', 11: 'a', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    out = []

    while value:
        bits = value & 15
        out.append(hex_chars.get(bits, bits))
        value >>= 4

    return '0x' + ''.join(map(str, reversed(out)))


N = 17
print(to_hex(N))
