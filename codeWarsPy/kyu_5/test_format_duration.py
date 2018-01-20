from unittest import TestCase

from kyu_5.HumanReadableDurationFormat import format_duration


class TestFormat_duration(TestCase):
    def test_format_duration(self):
        self.assertEqual(format_duration(1), "1 second")
        self.assertEqual(format_duration(62), "1 minute and 2 seconds")
        self.assertEqual(format_duration(120), "2 minutes")
        self.assertEqual(format_duration(3600), "1 hour")
        self.assertEqual(format_duration(3662), "1 hour, 1 minute and 2 seconds")
