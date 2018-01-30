from unittest import TestCase

from kyu_5.DoubleCola import whoIsNext


class TestWhoIsNext(TestCase):
    names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

    def test_whoIsNext0(self):
        self.assertEqual(whoIsNext(TestWhoIsNext.names, 1), "Sheldon")

    def test_whoIsNext01(self):
        self.assertEqual(whoIsNext(TestWhoIsNext.names, 4), TestWhoIsNext.names[3])

    def test_whoIsNext011(self):
        self.assertEqual(whoIsNext(TestWhoIsNext.names, 5), "Howard")

    def test_whoIsNext1(self):
        self.assertEqual(whoIsNext(TestWhoIsNext.names, 6), "Sheldon")

    def test_whoIsNext2(self):
        self.assertEqual(whoIsNext(TestWhoIsNext.names, 7), "Sheldon")

    def test_whoIsNext22(self):
        self.assertEqual(whoIsNext(TestWhoIsNext.names, 8), "Leonard")

    def test_whoIsNext23(self):
        self.assertEqual(whoIsNext(TestWhoIsNext.names, 9), "Leonard")

    def test_whoIsNext23312(self):
        self.assertEqual(whoIsNext(TestWhoIsNext.names, 13), "Rajesh")

    def test_whoIsNext233(self):
        self.assertEqual(whoIsNext(TestWhoIsNext.names, 14), "Howard")

    def test_whoIsNext2333(self):
        self.assertEqual(whoIsNext(TestWhoIsNext.names, 15), "Howard")

    def test_whoIsNext3(self):
        self.assertEqual(whoIsNext(TestWhoIsNext.names, 52), "Penny")

    def test_whoIsNext4(self):
        self.assertEqual(whoIsNext(TestWhoIsNext.names, 7230702951), "Leonard")
