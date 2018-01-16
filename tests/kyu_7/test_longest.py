from unittest import TestCase

from kyu_7.TwoToOne import longest


class TestLongest(TestCase):
    def test_longest(self):
        self.assert_equals = self.assertEqual
        self.assert_equals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
        self.assert_equals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
        self.assert_equals(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")
