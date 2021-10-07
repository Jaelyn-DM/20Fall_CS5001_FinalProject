'''
Duo Ma (Jaelyn)
CS5001 Fall 2020
Homework#9 Ciphers Part-2
Substitution Cipher Test- this is a program that test if substitution cipher
runs well in different scenarios, using unittest method
'''


from beale import encrypt
from beale import decrypt
import unittest


class BealeTest(unittest.TestCase):
    '''
    this is a unittest program to test if Beale Cioher's encrypt() and
    decrypt() works well in vairous scenarios
    '''
    def test_encrypt(self):
        '''
        this is a unittest to test if the encrypt() function in Beale.py
        runs well in different scenarios
        '''
        # test 1
        pt1 = 'secret'
        file1 = 'cipherpage.txt'
        seed1 = 10
        actual1 = encrypt(pt1, file1, seed1)
        expected1 = '1 4 2 5 6 3'
        self.assertEqual(actual1, expected1)

        # test 2
        pt2 = 'what what'
        file2 = 'catinthehat.txt'
        seed2 = 10
        actual2 = encrypt(pt2, file2, seed2)
        expected2 = '40 986 1522 1532 1055 1002 1525 1537'
        self.assertEqual(actual2, expected2)

        # test 3
        pt3 = 'helloworld'
        file3 = 'text_full_repeat.txt'
        seed3 = 3
        actual3 = encrypt(pt3, file3, seed3)
        expected3 = '8 5 12 38 15 23 41 18 64 4'
        self.assertEqual(actual3, expected3)

        # test 4
        pt4 = 'abcde'
        file4 = 'text_half.txt'
        seed4 = 4
        actual4 = encrypt(pt4, file4, seed4)
        expected4 = '1 2 3 4 5'
        self.assertEqual(actual4, expected4)

        # test 5
        pt5 = 'Hello Jaelyn'
        file5 = 'text_full_repeat.txt'
        seed5 = 5
        actual5 = encrypt(pt5, file5, seed5)
        expected5 = '60 57 64 38 67 62 53 31 12 77 66'
        self.assertEqual(actual5, expected5)

        # test 6
        pt6 = 'I love CS'
        file6 = 'text_full_num.txt'
        seed6 = 6
        actual6 = encrypt(pt6, file6, seed6)
        expected6 = '10 14 17 25 6 4 22'
        self.assertEqual(actual6, expected6)

    def test_encrypt_error1(self):
        '''
        this function is to test if the encrypt() raises correct error when the
        words in key is not enough to cover the repeating letters in plaintext
        '''
        try:
            encrypt('secrets', 'cipherpage.txt', 10)
            self.fail('Failed: no error was raised')
        except ValueError as ex:
            if str(ex) != 'Key file does not have enough words':
                self.fail('Failed: error raised wrong message')
        else:
            self.fail('Failed: wrong error was raised')

    def test_encrypt_error2(self):
        '''
        this function is to test if the enrypt() raises correct error when the
        words in key file is not enough to cover the letters in plaintext.
        '''
        try:
            pt2 = 'abcxyz'
            file2 = 'text_half.txt'
            seed2 = 2
            encrypt(pt2, file2, seed2)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Key file does not have enough words':
                self.fail('Failed: wrong message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error3(self):
        '''
        this function is to test if the encrypt() raises correct error when the
        letters in key has full alphabet but not covered the repeating ones
        '''
        try:
            pt3 = 'hello, hello'
            file3 = 'text_full.txt'
            seed3 = 3
            encrypt(pt3, file3, seed3)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Key file does not have enough words':
                self.fail('Failed: wrong message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error4(self):
        '''
        this function is to test if the encrypt() raises correct error when the
        plaintext passed in is not a string
        '''
        try:
            pt4 = 123
            file4 = 'text_full.txt'
            seed4 = 4
            encrypt(pt4, file4, seed4)
            self.fail('Failed: no error raised')
        except TypeError as ex:
            if str(ex) != 'plaintext should be a string':
                self.fail('Failed: wrong message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error5(self):
        '''
        this function is to test if the encrypt() raises correct error when the
        plaintext passed in is empty
        '''
        try:
            pt5 = ''
            file5 = 'text_full.txt'
            seed5 = 5
            encrypt(pt5, file5, seed5)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'plaintext should have at least 1 letter':
                self.fail('Failed: wrong message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error6(self):
        '''
        this function is to test if the encrypt() raises correct error when the
        plaintext passed in contains non-alphabetic characters
        '''
        try:
            pt6 = 'abcd123'
            file6 = 'text_full.txt'
            seed6 = 6
            encrypt(pt6, file6, seed6)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'all characters in plaintext should be alphabet':
                self.fail('Failed: wrong message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error7(self):
        '''
        this function is to test if the encrypt() raises correct error when the
        key_seed passed in contains non-digit characters
        '''
        try:
            pt7 = 'abcd'
            file7 = 'text_full.txt'
            seed7 = 'abc123'
            encrypt(pt7, file7, seed7)
            self.fail('Failed: no error raised')
        except TypeError as ex:
            if str(ex) != 'Numeric key should be an integer':
                self.fail('Failed: wrong message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error8(self):
        '''
        this function is to test if the encrypt() raises correct error when the
        key filename does not exist
        '''
        try:
            pt8 = 'abcd'
            file8 = 'text_full'
            seed8 = 8
            encrypt(pt8, file8, seed8)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Filename does not exist':
                self.fail('Failed: wrong message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error9(self):
        '''
        this function is to test if the encrypt() raises correct error when the
        key file contains numbers, but not enough letters for plaintext
        '''
        try:
            pt9 = 'hellowoworld'
            file9 = 'text_full_num.txt'
            seed9 = 9
            encrypt(pt9, file9, seed9)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Key file does not have enough words':
                self.fail('failed:wrong message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt(self):
        '''
        this is a unittest to test if the decrypt() function in Beale.py
        runs well in different scenarios
        '''
        # test 1
        ct1 = '1 4 2 5 6 3'
        file1 = 'cipherpage.txt'
        actual1 = decrypt(ct1, file1)
        expected1 = 'secret'.upper()
        self.assertEqual(actual1, expected1)

        # test 2
        ct2 = '40 986 1522 1532 1055 1002 1525 1537'
        file2 = 'catinthehat.txt'
        actual2 = decrypt(ct2, file2)
        expected2 = 'WHATWHAT'
        self.assertEqual(actual2, expected2)

        # test 3
        ct3 = '8 5 12 38 15 23 41 18 64 4'
        file3 = 'text_full_repeat.txt'
        actual3 = decrypt(ct3, file3)
        expected3 = 'HELLOWORLD'
        self.assertEqual(actual3, expected3)

        # test 4
        ct4 = '1 2 3 4 5'
        file4 = 'text_half.txt'
        actual4 = decrypt(ct4, file4)
        expected4 = 'ABCDE'
        self.assertEqual(actual4, expected4)

        # test 5
        ct5 = '60 57 64 38 67 62 53 31 12 77 66'
        file5 = 'text_full_repeat.txt'
        actual5 = decrypt(ct5, file5)
        expected5 = 'HELLOJAELYN'
        self.assertEqual(actual5, expected5)

        # test 6
        ct6 = '1 27 2 3'
        file6 = 'text_full_repeat.txt'
        actual6 = decrypt(ct6, file6)
        expected6 = 'AABC'
        self.assertEqual(actual6, expected6)

        # test 7
        ct7 = '1 1 2 3'
        file7 = 'text_full.txt'
        actual7 = decrypt(ct7, file7)
        expected7 = 'AABC'
        self.assertEqual(actual7, expected7)

        # test 8
        ct8 = '10 14 17 25 6 4 22'
        file8 = 'text_full_num.txt'
        actual8 = decrypt(ct8, file8)
        expected8 = 'ILOVECS'
        self.assertEqual(actual8, expected8)

    def test_decrypt_error1(self):
        '''
        this function is to test if the decrypt() raises correct error when the
        words in key is not enough to cover the index in ciphertext
        '''
        try:
            ct1 = '1 28 35'
            file1 = 'text_half.txt'
            decrypt(ct1, file1)
            self.fail('Failed: no error was raised')
        except ValueError as ex:
            if str(ex) != 'Key does not have enough words':
                self.fail('Failed: error raised wrong message')
        else:
            self.fail('Failed: wrong error was raised')

    def test_decrypt_error2(self):
        '''
        this function is to test if the decrypt() raises correct error when the
        ciphertext passed in is not a string
        '''
        try:
            ct2 = 123
            file2 = 'text_full.txt'
            decrypt(ct2, file2)
            self.fail('Failed: no error raised')
        except TypeError as ex:
            if str(ex) != 'ciphertext should be a string':
                self.fail('Failed: wrong message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt_error3(self):
        '''
        this function is to test if the decrypt() raises correct error when the
        ciphertext passed in is empty
        '''
        try:
            ct3 = ''
            file3 = 'text_full.txt'
            decrypt(ct3, file3)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'ciphertext should have at least 1 letter':
                self.fail('Failed: wrong message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt_error4(self):
        '''
        this function is to test if the decrypt() raises correct error when the
        ciphertext passed in contains non-digit characters
        '''
        try:
            ct4 = 'abcd 12 3'
            file4 = 'text_full.txt'
            decrypt(ct4, file4)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'ciphertext should contains numbers only':
                self.fail('Failed: wrong message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt_error5(self):
        '''
        this function is to test if the encrypt() raises correct error when the
        key filename does not exist
        '''
        try:
            ct5 = '1 2 3 4'
            file5 = 'text_full'
            decrypt(ct5, file5)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Filename does not exist':
                self.fail('Failed: wrong message')
        else:
            self.fail('Failed: wrong error')


def main():
    unittest.main(verbosity=3)


if __name__ == '__main__':
    main()
