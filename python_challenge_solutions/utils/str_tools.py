import string as String
from random import randint, choice


def randomize_str(input_str):
    chars = [c for c in input_str]
    for i, value in enumerate(chars):

        rand_index = randint(i, len(input_str)-1)
        temp_chars = chars
        new_char = chars[rand_index]

        if value == ' ' or new_char == ' ':
            continue

        temp_chars[i] = new_char
        temp_chars[rand_index] = value
        chars = temp_chars

    return ''.join(chars)

def count_matching_chars(input_str):
    matches = {}
    for c in input_str:
        if c in matches.keys():
            matches[c] += 1
        else:
            matches[c] = 1
    return matches


def random_capitolize(string: str):
    result = ''
    min_num, max_num = 0, 2
    include_spaces = False
    for c in string:
        if c == ' ' and not include_spaces:
            result += ' '
            continue

        num = randint(min_num, max_num)
        if num == 0:
            result += c.upper()
        elif num == 1:
            result += c.lower()
        elif num == 2:
            result += choice(String.ascii_letters)
    return result