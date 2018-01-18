from unittest import TestCase

from kyu_6.FindTheMissingLetter import find_missing_letter


class TestFind_missing_letter(TestCase):
    def test_find_missing_letter(self):
        self.assert_equals = self.assertEqual
        self.assert_equals(find_missing_letter(['a', 'b', 'c', 'd', 'f']), 'e')
        self.assert_equals(find_missing_letter(['O', 'Q', 'R', 'S']), 'P')
