from unittest import TestCase

from kyu_5.PerimeterOfSquaresInARectangle import perimeter


class TestPerimeter(TestCase):
    def test_perimeter(self):
        self.assert_equals = self.assertEqual
        self.assert_equals(perimeter(5), 80)
        self.assert_equals(perimeter(7), 216)
        self.assert_equals(perimeter(20), 114624)
        self.assert_equals(perimeter(30), 14098308)
        self.assert_equals(perimeter(100), 6002082144827584333104)
