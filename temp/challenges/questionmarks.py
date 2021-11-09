# def QuestionsMarks(text: str):
#     last_digit = None
#     question_count = 0
#     valid = True
#     any_10 = False
#
#     for c in text:
#         question_count += c == '?'
#         # is c a number?
#         if c.isnumeric():
#             c = int(c)
#
#             # check if last_digit is not set
#             # set it if it is not set
#             if last_digit is None:
#                 last_digit = c
#                 question_count = 0
#                 continue
#
#             # see if there is any 10 sums at all
#             any_10 = any_10 or c + last_digit == 10
#
#             # check if its a 10 sum and it has a bad number of question marks
#             if c + last_digit == 10 and question_count != 3:
#                 valid = False
#                 break
#
#             # we ran into a digit, so reset the question_count to 0
#             question_count = 0
#             # store current digit as the last_digit for comparison later
#             last_digit = c
#
#     if not any_10:
#         return 'false'
#
#     return str(valid).lower()


# def QuestionsMarks(text):
#     pairs = [(mid.count('?') == 3, int(x), int(y))
#              for x, mid, y, in re.findall(r'(\d)(\D+?)(\d)', text)]
#
#     if not (ten_pairs := [pair for pair in pairs if sum(pair[1:]) == 10]):
#         return 'false'
#
#     print(ten_pairs)
#     return 'true' if all(map(itemgetter(0), ten_pairs)) else 'false'


def QuestionsMarks(text: str):
    import re
    matches = list(re.finditer('\d', text))
    any_10 = False
    for d1, d2 in zip(matches[:-1], matches[1:]):
        if int(d1[0]) + int(d2[0]) == 10:
            any_10 = True

            if text[d1.span()[1]:d2.span()[0]].count('?') != 3:
                return 'false'

    return 'true' if any_10 else 'false'


def test_valid_returns_true():
    s = 'acc?7??sss?3rr1??????5'
    assert QuestionsMarks(s) == 'true', f'{s!r} should be true'


def test_basic_returns_true():
    assert QuestionsMarks('1???9') == 'true', 'basic test "1???9" case should be true'


def test_false_1():
    s = 'aaaaaaarrrrr??????'
    assert QuestionsMarks(s) == 'false', f'{s!r} should be false'


def test_false_2():
    s = '9???1???9??1???9'
    assert QuestionsMarks(s) == 'false', f'{s!r} should be false'


def test_false_3():
    s = '5??aaaaaaaaaaaaaaaaaaa?5?5'
    assert QuestionsMarks(s) == 'false', f'{s!r} should be false'


def test_false_4():
    s = 'aa6?9'
    assert QuestionsMarks(s) == 'false', f'{s!r} should be false'
