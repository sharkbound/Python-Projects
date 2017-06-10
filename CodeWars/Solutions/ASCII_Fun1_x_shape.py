import unittest

def x(n):
    boxes, ret, first, second = ['■', '□'], [], 0, -1
    base = boxes[1] * n #python 2 solution-- base = [boxes[1] for _ in range(n)]

    for _ in range(n):
        t = list(base)
        t[first], t[second] = boxes[0], boxes[0]
        first, second = first + 1, second - 1
        ret.append(''.join(t))

    return '\n'.join(ret)

class test_ascii_fun_x_shape(unittest.TestCase):
    def test_n_is_3(self):
        self.assertEqual(x(3), "■□■\n□■□\n■□■", "Should look like this: \n■□■\n□■□\n■□■")

    def test_n_is_7(self):
        self.assertEqual(x(7), "■□□□□□■\n□■□□□■□\n□□■□■□□\n□□□■□□□\n□□■□■□□\n□■□□□■□\n■□□□□□■",
                         "Should look like this: \n■□□□□□■\n□■□□□■□\n□□■□■□□\n□□□■□□□\n□□■□■□□\n□■□□□■□\n■□□□□□■")
