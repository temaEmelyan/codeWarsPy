from unittest import TestCase

from kyu_6.FormatAStringOfNames import namelist


class TestNamelist(TestCase):
    def test_namelist(self):
        self.assert_equals = self.assertEqual
        self.assert_equals(
            namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]),
            'Bart, Lisa, Maggie, Homer & Marge',
            "Must work with many names")
        self.assert_equals(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
                           "Must work with many names")
        self.assert_equals(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]), 'Bart & Lisa',
                           "Must work with two names")
        self.assert_equals(namelist([{'name': 'Bart'}]), 'Bart', "Wrong output for a single name")
        self.assert_equals(namelist([]), '', "Must work with no names")
