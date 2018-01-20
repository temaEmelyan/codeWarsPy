from unittest import TestCase

from kyu_5.Rot13 import rot13


class TestRot13(TestCase):
    def test_rot13(self):
        self.assertEqual(rot13("test"), "grfg")
        self.assertEqual(rot13("Test"), "Grfg")
