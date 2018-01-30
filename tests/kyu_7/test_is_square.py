import random
from unittest import TestCase

from kyu_7.YouAreASquare import is_square


class TestIsSquare(TestCase):
    def test_func(self):
        self.assertTrue(not is_square(-1), "Negative numbers cannot be square numbers")
        self.assertTrue(not is_square(3))
        self.assertTrue(is_square(4))
        self.assertTrue(is_square(25))
        self.assertTrue(not is_square(26))

        for i in range(1, 100):
            r = random.randint(0, 0xfff0)
            self.assertTrue(is_square(r * r), "{number} is a square number".format(number=(r * r)))
