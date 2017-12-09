from unittest import TestCase

from day3.part1.day3part1 import step_count


class TestStep_count(TestCase):
    def test_1_returns_0(self):
        self.assertEqual(0, step_count(1))

    def test_12_returns_3(self):
        self.assertEqual(3, step_count(12))

    def test_23_returns_2(self):
        self.assertEqual(2, step_count(23))
        
    def test_1024_returns_31(self):
        self.assertEqual(31, step_count(1024))
