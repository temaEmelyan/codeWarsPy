import unittest
from random import randint

from kyu_6.ReplaceWithAlphabetPosition import alphabet_position, alphabet_position1


class MyTest(unittest.TestCase):

    def test_replace_with_alphabet(self):
        self.replace_with_alphabet(alphabet_position)

    def test_replace_with_alphabet1(self):
        self.replace_with_alphabet(alphabet_position1)

    def replace_with_alphabet(self, func):
        test = self
        test.assert_equals = test.assertEqual
        test.assert_equals(func("The sunset sets at twelve o' clock."),
                           "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
        test.assert_equals(func("The narwhal bacons at midnight."),
                           "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

        number_test = ""
        for item in range(10):
            number_test += str(randint(1, 9))
        test.assert_equals(func(number_test), "")
