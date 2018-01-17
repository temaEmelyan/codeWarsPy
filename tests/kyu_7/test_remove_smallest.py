from unittest import TestCase

from kyu_7.RemoveTheMinimum import remove_smallest


class TestRemove_smallest(TestCase):
    def test_remove_smallest(self):
        self.assert_equals = self.assertEqual
        self.assert_equals(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
        self.assert_equals(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
        self.assert_equals(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
        self.assert_equals(remove_smallest([]), [], "Wrong result for []")
