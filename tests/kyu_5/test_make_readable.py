from unittest import TestCase

from kyu_5.HumanReadableTime import make_readable


class TestMake_readable(TestCase):
    def test_make_readable(self):
        self.assert_equals = self.assertEqual
        self.assert_equals(make_readable(0), "00:00:00")
        self.assert_equals(make_readable(5), "00:00:05")
        self.assert_equals(make_readable(60), "00:01:00")
        self.assert_equals(make_readable(86399), "23:59:59")
        self.assert_equals(make_readable(359999), "99:59:59")
