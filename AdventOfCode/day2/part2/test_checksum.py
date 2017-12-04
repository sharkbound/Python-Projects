from unittest import TestCase
from day2.part2.day2part2 import checksum

lines = [
    [5, 9, 2, 8],
    [9, 4, 7, 3],
    [3, 8, 6, 5]
]


class TestChecksum(TestCase):
    def test_checksum(self):
        self.assertEqual(9, checksum(lines))
