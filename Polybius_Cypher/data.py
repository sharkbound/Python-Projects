import os, re

CYPHER = (
    ('A', 'B', 'C', 'D', 'E'),
    ('F', 'G', 'H', 'IJ', 'K'),
    ('L', 'M', 'N', 'O', 'P'),
    ('Q', 'R', 'S', 'T', 'U'),
    ('V', 'W', 'X', 'Y', 'Z'),

    (' ', '\n', '\t')
)
UNDEFINED_CHARATER_SYMBOL = '['


def encrypt(*chars):
    res = ''
    for c in map(str.upper, chars):
        found = False
        for i, r in enumerate(CYPHER):
            for j, v in enumerate(r):
                if v == c:
                    res += f'{i}{j}'
                    found = True
        if not found:
            res += UNDEFINED_CHARATER_SYMBOL + c
    return res

def decrypt(text):
    res = ''
    for v in (text[i:i + 2] for i in range(0, len(text), 2)):
        res += CYPHER[int(v[0])][int(v[1])] if v[0] != UNDEFINED_CHARATER_SYMBOL else v[1]
    return res
