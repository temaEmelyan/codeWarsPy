from unittest import TestCase

from kyu_6.CountingDuplicates import duplicate_count


class TestDuplicate_count(TestCase):
    def test_duplicate_count(self):
        self.assert_equals = self.assertEqual
        self.assert_equals(duplicate_count("abcde"), 0)
        self.assert_equals(duplicate_count("abcdea"), 1)
        self.assert_equals(duplicate_count("indivisibility"), 1)
        self.assert_equals(duplicate_count("Indivisibilities"), 2)
