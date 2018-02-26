from unittest import TestCase

from kyu_5.TypoglecemiaGenerator import scramble_words


class TestScramble_words(TestCase):
    def test_scramble_words(self):
        self.assert_equals = self.assertEqual
        self.assert_equals(scramble_words('professionals'), 'paefilnoorsss',
                           'The first and last letters of a word should reamin in place with the inner letters sorted')
        self.assert_equals(scramble_words('i'), 'i', 'Must handle single charater words')
        self.assert_equals(scramble_words(''), '', 'Must handle empty strings')
        self.assert_equals(scramble_words('me'), 'me', 'Must handle 2 charater words')
        self.assert_equals(scramble_words('you'), 'you', 'Must handle 3 charater words')
        self.assert_equals(scramble_words('card-carrying'), 'caac-dinrrryg',
                           'Only spaces separate words and punctuation should remain at the same place as it started')
        self.assert_equals(scramble_words("shan't"), "sahn't",
                           'Punctuation should remain at the same place as it started')
        self.assert_equals(scramble_words('-dcba'), '-dbca', 'Must handle special character at the start')
        self.assert_equals(scramble_words('dcba.'), 'dbca.', 'Must handle special character at the end')
        self.assert_equals(scramble_words(
            "you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth."),
            "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth.",
            'Must handle a full sentence')
