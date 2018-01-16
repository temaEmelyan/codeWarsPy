from unittest import TestCase

from kyu_7.highestAndLowest import high_and_low, high_and_low1


class TestHighAndLow(TestCase):

    def test_high_and_low(self):
        self.t_high_and_low(high_and_low)
        self.t_high_and_low(high_and_low1)

    def t_high_and_low(self, func):
        ae = self.assertEqual
        ae(func("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")
        ae(func("1 -1"), "1 -1")
        ae(func("1 1"), "1 1")
        ae(func("-1 -1"), "-1 -1")
        ae(func("1 -1 0"), "1 -1")
        ae(func("1 1 0"), "1 0")
        ae(func("-1 -1 0"), "0 -1")
        ae(func("42"), "42 42")
