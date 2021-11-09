from unittest import TestCase


def stairs(n):
    spaces, segments = '    ' * (n-1), []
    for x in range(1, n+1):
        left = ' '.join(str(y + 1)[-1] for y in range(x))
        segments.append(spaces + left + ' ' + left[::-1])
        spaces = spaces[0:-4]
    return '\n'.join(segments)


class unittest(TestCase):
    def test_n_is_3(self):
        print("Testing for n = 3")
        self.assertEqual(stairs(3), "        1 1\n    1 2 2 1\n1 2 3 3 2 1")

    def test_n_is_7(self):
        print("Testing for n = 7")
        self.assertEqual(stairs(7),
                         "                        1 1\n                    1 2 2 1\n                1 2 3 3 2 1\n            1 2 3 4 4 3 2 1\n        1 2 3 4 5 5 4 3 2 1\n    1 2 3 4 5 6 6 5 4 3 2 1\n1 2 3 4 5 6 7 7 6 5 4 3 2 1")
