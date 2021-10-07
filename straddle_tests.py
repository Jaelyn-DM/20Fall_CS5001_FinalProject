'''
Duo Ma (Jaelyn)
CS5001 2020 Fall
HW#9 Ciphers part 2
This unittest is to test if the Straddle Checkboard ciphers encrypt() and
decrypt() works well in various test cases
'''

from straddle import encrypt
from straddle import decrypt
import unittest


class StraddleTest(unittest.TestCase):
    '''
    this is to test if straddle encrypt() and decrypt() works well
    '''

    def test_encrypt(self):
        '''
        '''
        # test 1 given example in the hw description
        pt1 = 'Prof Jump is crazy to think we can do this!'
        key_word1 = 'NORTHEASBCDFGIJKLMPQUVWXYZ'
        key_num1 = 26
        key_adder1 = 38574
        actual1 = encrypt(pt1, key_word1, key_num1, key_adder1)
        expected1 = 'SAAAYNORXEOE0EEAEOTFNESSJAAETNEHEAFNEAAANN'
        self.assertEqual(actual1, expected1)

        # test 2 (raising error): passed in numeric key is a string
        pt2 = 'Prof Jump is crazy to think we can do this!'
        key_word2 = 'NORTHEASBCDFGIJKLMPQUVWXYZ'
        key_num2 = '2, 6'
        key_adder2 = 38574
        try:
            encrypt(pt2, key_word2, key_num2, key_adder2)
            self.fail('Failed: no error')
        except TypeError as ex:
            if str(ex) != 'Numeric key should be an integer':
                self.fail('Failed: wrong message')
        else:
            self.fail('Failed: wrong error')

        # test 3 (raising error): passed in adder key is a string
        pt3 = 'Prof Jump is crazy to think we can do this!'
        key_word3 = 'NORTHEASBCDFGIJKLMPQUVWXYZ'
        key_num3 = 26
        key_adder3 = '38574'
        try:
            encrypt(pt3, key_word3, key_num3, key_adder3)
            self.fail('Failed: no error')
        except TypeError as ex:
            if str(ex) != 'Numeric key should be an integer':
                self.fail('Failed: wrong message')
        else:
            self.fail('Failed: wrong error')

        # test 4: numeric keys are adjacent, e.g. 4, 5
        pt4 = 'Hello,world!'
        key4 = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num4 = 45
        key_adder4 = 123
        expected4 = 'VXTLS0UMULW0T'
        actual4 = encrypt(pt4, key4, key_num4, key_adder4)
        self.assertEqual(actual4, expected4)

        # test 5: numberic keys are adjacent, e.g. 2, 8
        pt5 = 'helloworld!!'
        key_word5 = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num5 = 28
        key_adder5 = 1
        actual5 = encrypt(pt5, key_word5, key_num5, key_adder5)
        expected5 = 'SYSWXTXTXWVXWXYXTSV'
        self.assertEqual(actual5, expected5)

        # test6: numberic keys are at begining, e.g. 0, 1
        pt6 = 'helloworld!!'
        key_word6 = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num6 = 12
        key_adder6 = 20
        actual6 = encrypt(pt6, key_word6, key_num6, key_adder6)
        expected6 = 'XZXYYVYVYYUMPJB'
        self.assertEqual(actual6, expected6)

        # test7: numberix keys are at end, e.g. 8 9
        pt7 = 'hello,world.'
        key_word7 = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num7 = 89
        key_adder7 = 1
        actual7 = encrypt(pt7, key_word7, key_num7, key_adder7)
        expected7 = 'ZYZVAADVDGAZU'
        self.assertEqual(actual7, expected7)

        # test 8 (raising error): key adder == 0
        pt8 = 'hellohello'
        key_word8 = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num8 = 89
        key_adder8 = 0
        try:
            encrypt(pt8, key_word8, key_num8, key_adder8)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'a valid adder should be a positive integer':
                self.fail('Fail: wrong error message')
        else:
            self.fail('Fail: wrong error')

        # test 9: key_adder is longer than the plaintext
        pt9 = 'helloworld!!'
        key_word9 = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num9 = 28
        key_adder9 = 12301230123012301230
        actual9 = encrypt(pt9, key_word9, key_num9, key_adder9)
        expected9 = 'SQXXCUXVTNWXKZT'
        self.assertEqual(actual9, expected9)

    def test_encrypt_error1(self):
        '''
        this is to test if the encrypt() raises correct error when the
        passed in plaintext is not a string
        '''
        pt = 123
        keyword = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num = 23
        key_adder = 12345
        try:
            encrypt(pt, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except TypeError as ex:
            if str(ex) != 'plaintext should be a string':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error2(self):
        '''
        this is to test if the encrypt() raises correct error when the
        passed in plaintext is empty
        '''
        pt = ''
        keyword = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num = 23
        key_adder = 12345
        try:
            encrypt(pt, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'plaintext should have at least 1 letter':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error3(self):
        '''
        this is to test if the encrypt() raises correct error when the
        passed in plaintext contains numbers
        '''
        pt = 'abcd124'
        keyword = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num = 23
        key_adder = 12345
        try:
            encrypt(pt, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'all characters in plaintext should be alphabet':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error4(self):
        '''
        this is to test if the encrypt() raises correct error when the
        passed in alphakey is not a string
        '''
        pt = 'helloworld'
        keyword = 12345
        key_num = 23
        key_adder = 12345
        try:
            encrypt(pt, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except TypeError as ex:
            if str(ex) != 'Alphabetic key should be a string':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error5(self):
        '''
        this is to test if the encrypt() raises correct error when the
        passed in alphakey is 26 in length
        '''
        pt = 'helloworld'
        keyword = 'ABCDEFGHJIKLMN'
        key_num = 23
        key_adder = 12345
        try:
            encrypt(pt, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Alphabetic key should contain 26 letters':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error6(self):
        '''
        this is to test if the encrypt() raises correct error when the
        passed in alphakey is contains non-alphabetic characters
        '''
        pt = 'helloworld'
        keyword = 'ABCDEFGHIJKLMNOPQRSTUVW123'
        key_num = 23
        key_adder = 12345
        try:
            encrypt(pt, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Alphabetic key should contain letters only':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error7(self):
        '''
        this is to test if the encrypt() raises correct error when the
        passed in alphakey is contains duplicated letters
        '''
        pt = 'helloworld'
        keyword = 'ABCDEFGHIJKLMABCDEFGHIJKLM'
        key_num = 23
        key_adder = 12345
        try:
            encrypt(pt, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'the alphabetic key should not conatin duplicates':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error8(self):
        '''
        this is to test if the encrypt() raises correct error when the
        passed in adder key is a negative integer
        '''
        pt = 'helloworld'
        keyword = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num = 23
        key_adder = -45222
        try:
            encrypt(pt, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'a valid adder should be a positive integer':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error9(self):
        '''
        this is to test if the encrypt() raises correct error when the
        passed in numeric key contains 0
        '''
        pt = 'helloworld'
        keyword = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num = 20
        key_adder = 34572
        try:
            encrypt(pt, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Numbers in numeric key should be greater than zero':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error10(self):
        '''
        this is to test if the encrypt() raises correct error when the
        passed in numeric key contains two same number
        '''
        pt = 'helloworld'
        keyword = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num = 33
        key_adder = 34572
        try:
            encrypt(pt, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Two numbers in numeric key should be distinct':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error11(self):
        '''
        this is to test if the encrypt() raises correct error when the
        passed in numeric key contains only 1 digit
        '''
        pt = 'helloworld'
        keyword = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num = 9
        key_adder = 34572
        try:
            encrypt(pt, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Numeric key should contain two digit':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_encrypt_error12(self):
        '''
        this is to test if the encrypt() raises correct error when the
        passed in numeric key contains 3 digit
        '''
        pt = 'helloworld'
        keyword = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num = 124
        key_adder = 34572
        try:
            encrypt(pt, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Numeric key should contain two digit':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt(self):
        '''
        this function is to test if decrypt() in Straddle cipher works well in
        various scenarios
        '''
        # test 1 given example in the hw description
        ct1 = 'SAAAYNORXEOE0EEAEOTFNESSJAAETNEHEAFNEAAANN'
        key_word1 = 'NORTHEASBCDFGIJKLMPQUVWXYZ'
        key_num1 = 26
        key_adder1 = 38574
        actual1 = decrypt(ct1, key_word1, key_num1, key_adder1)
        expected1 = 'ProfJumpiscrazytothinkwecandothi'.upper()
        self.assertEqual(actual1, expected1)

        # test 2: same test in webpage
        ct1 = 'SAAAYNORXEOE0EEAEOTFNESSJAAETNEHEAFNEAAANN'
        key_word1 = 'NORTHEASBCDFGIJKLMPQUVWXYZ'
        key_num1 = 26
        key_adder1 = 38574
        actual1 = decrypt(ct1, key_word1, key_num1, key_adder1)
        expected1 = 'ProfJumpiscrazytothinkwecandothi'.upper()
        self.assertEqual(actual1, expected1)

        # test 4: ciphertext contains '0' or '1'
        ct4 = 'VXTLS0UMULW0T'
        key4 = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num4 = 45
        key_adder4 = 123
        expected4 = 'HELLOWORL'
        actual4 = decrypt(ct4, key4, key_num4, key_adder4)
        self.assertEqual(actual4, expected4)

        # test 5: numberic keys are adjacent, e.g. 2, 8
        ct5 = 'SYSWXTXTXWVXWXYXTSV'
        key_word5 = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num5 = 28
        key_adder5 = 1
        actual5 = decrypt(ct5, key_word5, key_num5, key_adder5)
        expected5 = 'HELLOWORLD'
        self.assertEqual(actual5, expected5)

        # test6: numberic keys are at begining, e.g. 0, 1
        ct6 = 'XZXYYVYVYYUMPJB'
        key_word6 = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num6 = 12
        key_adder6 = 20
        actual6 = decrypt(ct6, key_word6, key_num6, key_adder6)
        expected6 = 'HELLOWORLD'
        self.assertEqual(actual6, expected6)

        # test7: numberix keys are at end, e.g. 8 9
        ct7 = 'ZYZVAADVDGAZU'
        key_word7 = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num7 = 89
        key_adder7 = 1
        actual7 = decrypt(ct7, key_word7, key_num7, key_adder7)
        expected7 = 'HELLOWORLD'
        self.assertEqual(actual7, expected7)

        # test 8 (raising error): key adder == 0
        ct8 = 'hellohello'
        key_word8 = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num8 = 89
        key_adder8 = 0
        try:
            decrypt(ct8, key_word8, key_num8, key_adder8)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'a valid adder should be a positive integer':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: Wrong error')

        # test 9: key_adder is longer than the plaintext
        ct9 = 'SQXXCUXVTNWXKZT'
        key_word9 = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num9 = 28
        key_adder9 = 12301230123012301230
        actual9 = decrypt(ct9, key_word9, key_num9, key_adder9)
        expected9 = 'HELLOWORLD'
        self.assertEqual(actual9, expected9)

    def test_decrypt_error1(self):
        '''
        this is to test if the decrypt() raises correct error when the
        passed in ciphertext is not a string
        '''
        ct = 123
        keyword = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num = 23
        key_adder = 12345
        try:
            decrypt(ct, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except TypeError as ex:
            if str(ex) != 'ciphertext should be a string':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt_error2(self):
        '''
        this is to test if the decrypt() raises correct error when the
        passed in ciphertext is empty
        '''
        ct = ''
        keyword = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num = 23
        key_adder = 12345
        try:
            decrypt(ct, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'ciphertext should have at least 1 letter':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt_error3(self):
        '''
        this is to test if the decrypt() raises correct error when the
        passed in ciphertext contains numbers
        '''
        ct = 'abcd124'
        keyword = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num = 23
        key_adder = 12345
        try:
            decrypt(ct, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'all characters in ciphertext should be alphabet':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt_error4(self):
        '''
        this is to test if the decrypt() raises correct error when the
        passed in alphakey is not a string
        '''
        ct = 'helloworld'
        keyword = 12345
        key_num = 23
        key_adder = 12345
        try:
            decrypt(ct, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except TypeError as ex:
            if str(ex) != 'Alphabetic key should be a string':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt_error5(self):
        '''
        this is to test if the decrypt() raises correct error when the
        passed in alphakey is 26 in length
        '''
        ct = 'helloworld'
        keyword = 'ABCDEFGHJIKLMN'
        key_num = 23
        key_adder = 12345
        try:
            decrypt(ct, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Alphabetic key should contain 26 letters':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt_error6(self):
        '''
        this is to test if the decrypt() raises correct error when the
        passed in alphakey is contains non-alphabetic characters
        '''
        ct = 'helloworld'
        keyword = 'ABCDEFGHIJKLMNOPQRSTUVW123'
        key_num = 23
        key_adder = 12345
        try:
            decrypt(ct, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Alphabetic key should contain letters only':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt_error7(self):
        '''
        this is to test if the decrypt() raises correct error when the
        passed in alphakey is contains duplicated letters
        '''
        ct = 'helloworld'
        keyword = 'ABCDEFGHIJKLMABCDEFGHIJKLM'
        key_num = 23
        key_adder = 12345
        try:
            decrypt(ct, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'the alphabetic key should not conatin duplicates':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt_error8(self):
        '''
        this is to test if the decrypt() raises correct error when the
        passed in adder key is a negative integer
        '''
        ct = 'helloworld'
        keyword = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num = 23
        key_adder = -45222
        try:
            decrypt(ct, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'a valid adder should be a positive integer':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt_error9(self):
        '''
        this is to test if the decrypt() raises correct error when the
        passed in numeric key contains 0
        '''
        ct = 'helloworld'
        keyword = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num = 20
        key_adder = 34572
        try:
            decrypt(ct, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Numbers in numeric key should be greater than zero':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt_error10(self):
        '''
        this is to test if the decrypt() raises correct error when the
        passed in numeric key contains two same number
        '''
        ct = 'helloworld'
        keyword = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num = 33
        key_adder = 34572
        try:
            decrypt(ct, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Two numbers in numeric key should be distinct':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt_error11(self):
        '''
        this is to test if the decrypt() raises correct error when the
        passed in numeric key contains only 1 digit
        '''
        ct = 'helloworld'
        keyword = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num = 9
        key_adder = 34572
        try:
            decrypt(ct, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Numeric key should contain two digit':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')

    def test_decrypt_error12(self):
        '''
        this is to test if the decrypt() raises correct error when the
        passed in numeric key contains 3 digit
        '''
        ct = 'helloworld'
        keyword = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        key_num = 124
        key_adder = 34572
        try:
            decrypt(ct, keyword, key_num, key_adder)
            self.fail('Failed: no error raised')
        except ValueError as ex:
            if str(ex) != 'Numeric key should contain two digit':
                self.fail('Failed: wrong error message')
        else:
            self.fail('Failed: wrong error')


def main():
    unittest.main(verbosity=3)


if __name__ == '__main__':
    main()
