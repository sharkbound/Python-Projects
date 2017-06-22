import random
import unittest
from itertools import permutations as perms


def permutations(s):
    return [''.join(x) for x in sorted(set(perms(s)))]


class PermutationTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(sorted(permutations('a')), ['a'])

    def test2(self):
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])

    def test3(self):
        self.assertEqual(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])

    def test3(self):
        self.assertEqual(permutations('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test4(self):
        self.assertEqual(permutations('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test5(self):
        self.assertEqual(permutations('abcd'),
                         ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac',
                          'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca',
                          'dcab', 'dcba'])


if __name__ == '__main__':
    unittest.main()
