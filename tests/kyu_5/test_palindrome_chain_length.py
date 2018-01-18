from unittest import TestCase

from kyu_5.PalindromeChainLength import palindrome_chain_length


class TestPalindrome_chain_length(TestCase):
    def test_palindrome_chain_length(self):
        self.assertEqual(palindrome_chain_length(87), 4)
