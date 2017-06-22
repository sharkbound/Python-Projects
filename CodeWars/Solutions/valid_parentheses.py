import unittest
import re


def valid_parentheses(s):
    if s.count('(') != s.count(')'):  return False
    if len(s) == 0: return True
    b = 0

    for c in re.sub(r'[^\(\)]', '', s):
        b += 1 if c == '(' else -1
        if b < 0:
            return False
    return True


class TestValidParentheses(unittest.TestCase):
    def test_only_tight(self):
        self.assertEqual(valid_parentheses("  ("), False)

    def test_only_left_words(self):
        self.assertEqual(valid_parentheses(")test"), False)

    def test_empty_str(self):
        self.assertEqual(valid_parentheses(""), True)

    def test_opposite(self):
        self.assertEqual(valid_parentheses("hi())("), False)

    def test_matching_with_words(self):
        self.assertEqual(valid_parentheses("hi(hi)()"), True)


if __name__ == '__main__':
    unittest.main()
