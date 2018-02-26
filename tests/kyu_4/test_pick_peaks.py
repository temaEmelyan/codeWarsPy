from unittest import TestCase

from kyu_4.PickPeaks import pick_peaks


class TestPickPeaks(TestCase):
    def test_pick_peaks(self):
        self.assert_equals = self.assertEqual
        self.assert_equals(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]), {"pos": [3, 7], "peaks": [6, 3]})

        self.assert_equals(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]), {"pos": [3, 7], "peaks": [6, 3]})

        self.assert_equals(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]),
                           {"pos": [3, 7, 10], "peaks": [6, 3, 2]})

        self.assert_equals(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2, 1]), {"pos": [2, 4], "peaks": [3, 2]})

        self.assert_equals(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]), {"pos": [2], "peaks": [3]})
