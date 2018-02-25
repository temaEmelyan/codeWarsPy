from unittest import TestCase

from kyu_6.BitCounting import countBits


class TestCountBits(TestCase):
    def test_countBits(self):
        self.assert_equals = self.assertEqual
        self.assert_equals(countBits(0), 0)
        self.assert_equals(countBits(4), 1)
        self.assert_equals(countBits(7), 3)
        self.assert_equals(countBits(9), 2)
        self.assert_equals(countBits(10), 2)
