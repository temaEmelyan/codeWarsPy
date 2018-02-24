from unittest import TestCase

from kyu_4.Permutations import permutations


class TestPermutations(TestCase):
    def test_permutations(self):
        self.assert_equals = self.assertEqual
        self.assert_equals(sorted(permutations('a')), ['a'])
        self.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
        self.assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
