'''
Duo Ma (Jaelyn)
CS5001 Fall 2020
Homework#9 Ciphers Part-2
Substitution Cipher Test- this is a program that test if substitution cipher
runs well in different scenarios, using unittest method
'''

from utils import strip
from utils import standard_format
from substitution import encrypt
from substitution import decrypt
import unittest


class SubstitutionTest(unittest.TestCase):
    '''
    this is a unittest program to test if Substitution Cipher's Encrypt()
    works well in substitution.py
    '''

    def test_encrypt(self):
        '''
        this is a unittest to test if the encrypt() function in
        substitution.py runs well in different scenarios
        '''
        # test 1: given test in hw description
        pt1 = 'Prof Jump is crazy to think we can do this!'
        key1 = 'ZECTPMSHAXFVRQBWILUGKJODYN'
        expected1 = strip('wlbm xkrw au clzny gb ghaqf op czq tb ghau').upper()
        actual1 = encrypt(pt1, key1)
        self.assertEqual(actual1, expected1)

        # test 2: plaintext with punctuations
        pt2 = 'Oh hi!!!hello, world!'
        key2 = 'lfxcepjsbkqdhizrogunywamtv'
        actual2 = encrypt(pt2, key2)
        expected2 = standard_format('zssbs eddza zgdc')
        self.assertEqual(actual2, expected2)

        # test 3: full alphabet as plaintext
        pt3 = 'abcdefghijklmnopqrstuvwxyz'
        key3 = 'sxzgjlfkeowpqbvatrndhycmiu'
        actual3 = encrypt(pt3, key3)
        expected3 = standard_format('sxzgjlfkeowpqbvatrndhycmiu')
        self.assertEqual(actual3, expected3)

        # test 4: key is ordered full alphabet letters
        # (in this case, a reminder should be printed)
        pt4 = 'this... is? a -- random !! test.'
        key4 = 'abcdefghijklmnopqrstuvwxyz'
        actual4 = encrypt(pt4, key4)
        expected4 = standard_format('thisisarandomtest')
        self.assertEqual(actual4, expected4)

        # test 5: given example in the webpage
        pt5 = 'defend the east wall of the castle'
        key5 = 'phqgiumeaylnofdxjkrcvstzwb'
        actual5 = encrypt(pt5, key5)
        expected5 = standard_format('giuifg cei iprc tpnn du cei qprcni')
        self.assertEqual(actual5, expected5)

        # test 6: plaintext only contains 1 letter
        pt6 = 'aaa'
        key6 = 'qazwsxedcrfvtgbyhnujmikolp'
        actual6 = encrypt(pt6, key6)
        expected6 = standard_format('qqq')
        self.assertEqual(actual6, expected6)

    def test_encrypt_error1(self):
        '''
        this unitest is to test if encrypt() raises correct error when the
        key passed in is not a string
        '''
        try:
            encrypt('helloworld', 12)
            self.fail('Failed with no error raised')
        except TypeError as ex:
            if str(ex) != 'Alphabetic key should be a string':
                self.fail('Failed with wrong error message')
        else:
            self.fail('Failed with wrong error raised')

    def test_encrypt_error2(self):
        '''
        this unittest is to test if encrypt() raises correct error when the
        key passed in does not have length of 26
        '''
        try:
            encrypt('helloworld', 'abcdefg')
            self.fail('Failed with no error raised')
        except ValueError as ex:
            if str(ex) != 'Alphabetic key should contain 26 letters':
                self.fail('Failed with wrong error message')
        else:
            self.fail('Failed with wrong error raised')

    def test_encrypt_error3(self):
        '''
        this unittest is to test if encrypt() raises correct error when the
        passed in key contains non-alphabetic elements
        '''
        try:
            encrypt('helloworld', '123defghijklmnopqrstuvwxyz')
            self.fail('failed with no error raised')
        except ValueError as ex:
            if str(ex) != 'Alphabetic key should contain letters only':
                self.fail('Failed with wrong message raised')
        else:
            self.fail('Failed with wrong error raised')

    def test_encrypt_error4(self):
        '''
        this unittest is to test if encrypt() raises correct error when
        the passed in key does not cover the full 26 letters
        '''
        try:
            encrypt('helloworld', 'abcdefghijklmabcdefghijklm')
            self.fail('Failed with no error raised')
        except ValueError as ex:
            if str(ex) != 'the alphabetic key should not conatin duplicates':
                self.fail('Failed with wrong message raised')
        else:
            self.fail('Failed with wrong error raised')

    def test_encrypt_error5(self):
        '''
        this unittest is to test if encrypt() raises correct error when the
        passed in plaintext is not a string
        '''
        try:
            encrypt(['helloworld'], 'QAZWSXEDCRFVTGBYHNUJMIKOLP')
            self.fail('Failed: no error raised')
        except TypeError as ex:
            if str(ex) != 'plaintext should be a string':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error6(self):
        '''
        this unittest is to test if encrypt() raises correct error when the
        passed in plaintext is an empty string
        '''
        try:
            encrypt('', 'QAZWSXEDCRFVTGBYHNUJMIKOLP')
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'plaintext should have at least 1 letter':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error7(self):
        '''
        this unittest is to test if encrypt() raises correct error when the
        passed in plaintext contains non-letter characters
        '''
        try:
            encrypt('hello123', 'QAZWSXEDCRFVTGBYHNUJMIKOLP')
            self.fail('Failed: no error')
        except ValueError as ex:
            if str(ex) != 'all characters in plaintext should be alphabet':
                self.fail('Failed: wrong message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt(self):
        '''
        this is a unittest to test if the encrypt() function in
        substitution.py runs well in different scenarios
        '''
        # test 1: given test in hw description
        ct1 = 'WLBMXKRWAUCLZNYGBGHAQFOPCZQTBGHAU'
        key1 = 'ZECTPMSHAXFVRQBWILUGKJODYN'
        expected1 = 'ProfJumpiscrazytothinkwecandothis'.upper()
        actual1 = decrypt(ct1, key1)
        self.assertEqual(actual1, expected1)

        # test 2：key is full alphabet in order
        ct2 = 'helloworld'
        key2 = 'abcdefghijklmnopqrstuvwxyz'
        expected2 = 'helloworld'.upper()
        actual2 = decrypt(ct2, key2)
        self.assertEqual(actual2, expected2)

        # test 3: given example from the webpage
        ct3 = 'giuifg cei iprc tpnn du cei qprcni'
        key3 = 'phqgiumeaylnofdxjkrcvstzwb'
        expected3 = standard_format('defend the east wall of the castle')
        actual3 = decrypt(ct3, key3)
        self.assertEqual(actual3, expected3)

        # test 4: cipher text contains only 1 letter:
        ct4 = 'xxx'
        key4 = 'qazxswedcvfrtgbnhyujmkiolp'
        expected4 = standard_format('ddd')
        actual4 = decrypt(ct4, key4)
        self.assertEqual(actual4, expected4)

    def test_decrypt_error1(self):
        '''
        this unitest is to test if decrypt() raises correct error when the
        key passed in is not a string
        '''
        try:
            decrypt('helloworld', 12)
            self.fail('Failed: no error raised')
        except TypeError as ex:
            if str(ex) != 'Alphabetic key should be a string':
                self.fail('Failed with wrong error message')
        else:
            self.fail('Failed with wrong error raised')

    def test_decrypt_error2(self):
        '''
        this unittest is to test if decrypt() raises correct error when the
        key passed in does not have length of 26
        '''
        try:
            decrypt('helloworld', 'abcdefg')
            self.fail('Failed with no error raised')
        except ValueError as ex:
            if str(ex) != 'Alphabetic key should contain 26 letters':
                self.fail('Failed with wrong error message')
        else:
            self.fail('Failed with wrong error raised')

    def test_decrypt_error3(self):
        '''
        this unittest is to test if decrypt() raises correct error when the
        passed in key contains non-letter elements
        '''
        try:
            decrypt('helloworld', '123defghijklmnopqrstuvwxyz')
            self.fail('failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Alphabetic key should contain letters only':
                self.fail('Failed: wrong message raised')
        else:
            self.fail('Failed: wrong error raised')

    def test_decrypt_error4(self):
        '''
        this unittest is to test if decrypt() raises correct error when
        the passed in key does not cover the full 26 letters
        '''
        try:
            decrypt('helloworld', 'abcdefghijklmabcdefghijklm')
            self.fail('Failed with no error raised')
        except ValueError as ex:
            if str(ex) != 'the alphabetic key should not conatin duplicates':
                self.fail('Failed with wrong message raised')
        else:
            self.fail('Failed with wrong error raised')

    def test_decrypt_error5(self):
        '''
        this unittest is to test if decrypt() raises correct error when the
        passed in ciphertext is not a string
        '''
        try:
            decrypt(123, 'QAZWSXEDCRFVTGBYHNUJMIKOLP')
            self.fail('Failed: no error raised')
        except TypeError as ex:
            if str(ex) != 'ciphertext should be a string':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt_error6(self):
        '''
        this unittest is to test if decrypt() raises correct error when the
        passed in ciphertext is an empty string
        '''
        try:
            decrypt('', 'QAZWSXEDCRFVTGBYHNUJMIKOLP')
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'ciphertext should have at least 1 letter':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt_error7(self):
        '''
        this unittest is to test if decrypt() raises correct error when the
        passed in ciphertext contains non-letter characters
        '''
        try:
            decrypt('hello123', 'QAZWSXEDCRFVTGBYHNUJMIKOLP')
            self.fail('Failed: no error')
        except ValueError as ex:
            if str(ex) != 'all characters in ciphertext should be alphabet':
                self.fail('Failed: wrong message')
        else:
            self.fail('Failed: wrong error')


def main():
    unittest.main(verbosity=3)


if __name__ == "__main__":
    main()
