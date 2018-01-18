from unittest import TestCase

from kyu_5.GapInPrimes import gap


class TestGap(TestCase):
    def test_gap(self):
        self.assert_equals = self.assertEqual
        self.assert_equals(gap(2, 100, 110), [101, 103])
        self.assert_equals(gap(4, 100, 110), [103, 107])
        self.assert_equals(gap(6, 100, 110), None)
        self.assert_equals(gap(8, 300, 400), [359, 367])
        self.assert_equals(gap(10, 300, 400), [337, 347])
