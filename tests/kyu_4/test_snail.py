from unittest import TestCase

from kyu_4.SnailSort import snail


class TestSnail(TestCase):
    def test_snail(self):
        self.assert_equals = self.assertEqual

        array = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assert_equals(snail(array), expected)

        array = [[1, 2, 3],
                 [8, 9, 4],
                 [7, 6, 5]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assert_equals(snail(array), expected)
