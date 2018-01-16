from unittest import TestCase

from kyu_7.SquareDigits import square_digits


class TestSquare_digits(TestCase):
    def test_square_digits(self):
        self.assertEqual(square_digits(9119), 811181)
