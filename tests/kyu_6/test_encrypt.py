from unittest import TestCase

from kyu_6.SimpleEncryption1AlternatingSplit import encrypt, decrypt


class TestEncrypt(TestCase):
    def test_encrypt(self):
        self.assert_equals = self.assertEqual
        self.assert_equals(encrypt("This is a test!", 0), "This is a test!")
        self.assert_equals(encrypt("This is a test!", 1), "hsi  etTi sats!")
        self.assert_equals(encrypt("This is a test!", 2), "s eT ashi tist!")
        self.assert_equals(encrypt("This is a test!", 3), " Tah itse sits!")
        self.assert_equals(encrypt("This is a test!", 4), "This is a test!")
        self.assert_equals(encrypt("This is a test!", -1), "This is a test!")
        self.assert_equals(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

        self.assert_equals(decrypt("This is a test!", 0), "This is a test!")
        self.assert_equals(decrypt("hsi  etTi sats!", 1), "This is a test!")
        self.assert_equals(decrypt("s eT ashi tist!", 2), "This is a test!")
        self.assert_equals(decrypt(" Tah itse sits!", 3), "This is a test!")
        self.assert_equals(decrypt("This is a test!", 4), "This is a test!")
        self.assert_equals(decrypt("This is a test!", -1), "This is a test!")
        self.assert_equals(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

        self.assert_equals(encrypt("", 0), "")
        self.assert_equals(decrypt("", 0), "")
        self.assert_equals(encrypt(None, 0), None)
        self.assert_equals(decrypt(None, 0), None)
