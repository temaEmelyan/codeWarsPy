from unittest import TestCase

from kyu_6.ReversedWords import reverseWords


class TestReverseWords(TestCase):
    def test_reverseWords(self):
        self.assertEqual(reverseWords("hello world!"), "world! hello")
