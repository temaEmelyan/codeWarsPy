from unittest import TestCase

from kyu_7.BinaryAddition import add_binary


class TestAdd_binary(TestCase):
    def test_add_binary(self):
        self.assert_equals = self.assertEqual
        self.assert_equals(add_binary(1, 1), "10")
        self.assert_equals(add_binary(0, 1), "1")
        self.assert_equals(add_binary(1, 0), "1")
        self.assert_equals(add_binary(2, 2), "100")
        self.assert_equals(add_binary(51, 12), "111111")
