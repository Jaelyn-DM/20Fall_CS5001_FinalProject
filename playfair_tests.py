'''
Duo Ma (Jaelyn)
CS5001 Fall 2020
HW#8 Playfair Cipher test
this program implement test cases for Playfair Cipher
encryptions and decryption functions
'''


from playfair import encrypt
from playfair import decrypt


def test_encrypt(plaintext, key, expected):
    '''
    name: test_encrypt
    parameter: plaintext: string that to be encoded by playfair cipher; key: a
    keyword string; expected: string that expected to be returned from encrypt
    return: True if actual ciphertext matches the expected; False otherwise
    '''
    actual = encrypt(plaintext, key)
    return actual == expected


def run_tests_encrypt():
    '''
    name: run_tests_encrypt()
    parameter: none
    return: number of failed test cases
    '''
    print('\nStart tesitng Playfair Cipher Encrypt...\n')
    fail_count = 0

    # test 1
    pt1 = 'Prof Jump is crazy to think we can do this'
    key1 = 'Northeastern'
    ct1 = 'XSAMKQPQGBSHCWTBRHTKHDVAESELRHTKGR'

    if test_encrypt(pt1, key1, ct1):
        print('test 1 passed')
    else:
        print('test 1 failed')
        fail_count += 1

    # test 2
    pt2 = 'helloworld'
    key2 = 'abcdefghijklmnopqrstuvwxyzabcde'
    ct2 = 'KCNVMYMTOA'

    if test_encrypt(pt2, key2, ct2):
        print('test 2 passed')
    else:
        print('test 2 failed')
        fail_count += 1

    # test 3
    pt3 = 'abbccxxx'
    key3 = 'abcde'
    ct3 = 'BCCDHCYY'.upper()
    if test_encrypt(pt3, key3, ct3):
        print('test 3 passed')
    else:
        print('test 3 failed')
        fail_count += 1

    # test 4
    pt4 = 'aabbccddx'
    key4 = 'aligner'
    ct4 = 'IVKIBYBZYY'
    if test_encrypt(pt4, key4, ct4):
        print('test 4 passed')
    else:
        print('test 4 failed')
        fail_count += 1

    # test 5
    pt5 = 'aaaaabbbbbccccc'
    key5 = 'aligner'
    ct5 = 'IVIVIEKIKIBYBYBY'
    if test_encrypt(pt5, key5, ct5):
        print('test 5 passed')
    else:
        print('test 5 failed')
        fail_count += 1

    # test 6
    pt6 = 'axxxx'
    key6 = 'abcde'
    ct6 = 'CVYYYY'
    if test_encrypt(pt6, key6, ct6):
        print('test 6 passed')
    else:
        print('test 6 failed')
        fail_count += 1

    return fail_count


def test_decrypt(ciphertext, key, expected):
    '''
    name: test_decrypt
    parameter: cipheretxt(stribg) to be decrypted by playfair ciphers;
    key (string); expected plaintext decrypted by playfair ciphers
    return: True if actual matches the expected plaintext; False otherwise
    '''
    actual = decrypt(ciphertext, key)
    return actual == expected


def run_tests_decrypt():
    '''
    name: run_tests_decrypt
    parameter: none
    return: number of failed test cases
    '''
    print('\nStart testing Playfair decrypt...')
    fail_count = 0

    # test 1
    ct1 = 'IVIVIEKIKIBYBYBY'
    key1 = 'aligner'
    pt1 = 'AXAXABBXBXCXCXCX'
    if test_decrypt(ct1, key1, pt1):
        print('test 1 passed')
    else:
        print('test 1 failed')
        fail_count += 1

    # test 2
    ct2 = 'XSAMKQPQGBSHCWTBRHTKHDVAESELRHTKGR'
    key2 = 'northeastern'
    pt2 = 'PROFIUMPISCRAZYTOTHINKWECANDOTHISX'
    if test_decrypt(ct2, key2, pt2):
        print('test 2 passed')
    else:
        print('test 2 failed')
        fail_count += 1

    # test 3
    ct3 = 'BXYYYY'
    key3 = 'xyz'
    pt3 = 'abxxxx'.upper()
    if test_decrypt(ct3, key3, pt3):
        print('test 3 passed')
    else:
        print('test 3 failed')
        fail_count += 1

    # test 4
    pt4 = 'AXBXCXDXXX'.upper()
    key4 = 'xyz'
    ct4 = 'BYXYHCCYYY'
    if test_decrypt(ct4, key4, pt4):
        print('test 4 passed')
    else:
        print('test 4 failed')
        fail_count += 1

    # test 5
    pt5 = 'AXAXABBXBXCXCXCX'
    key5 = 'xyz'
    ct5 = 'BYBYBXXYXYHCHCHC'
    if test_decrypt(ct5, key5, pt5):
        print('test 5 passed')
    else:
        print('test 5 failed')
        fail_count += 1

    # test 6
    pt6 = 'abbccdde'.upper()
    key6 = 'xyz'
    ct6 = 'BXXGDEEF'
    if test_decrypt(ct6, key6, pt6):
        print('test 6 passed')
    else:
        print('test 6 failed')
        fail_count += 1

    return fail_count


def error_test1():
    '''
    name: error_tests
    parameter: none
    return: number of failed cases for TypeError(key) in encrypt()
    '''
    fail_count = 0
    try:
        pt1 = 'abcd'
        key1 = 12
        encrypt(pt1, key1)
        print('failed because it did not raise the error\n')
        fail_count += 1
    except TypeError as ex:
        if str(ex) == 'key should be a string':
            print('error test 1 passed\n')
        else:
            print('test 1 failed with wrong error message\n')
            fail_count += 1
    except Exception:
        print('test 1 failed with worng error raised\n')
        fail_count += 1

    return fail_count


def error_test2():
    '''
    name: error_test2
    parameter: none
    return: number of failed cases for TypeError(plaintext) in encrypt()
    '''
    fail_count = 0
    try:
        pt2 = 1234
        key2 = 2
        encrypt(pt2, key2)
        print('failed because it did not raise the error\n')
        fail_count += 1
    except TypeError as ex:
        if str(ex) == 'plaintext should be a string':
            print('error test 2 passed\n')
        else:
            print('test 2 failed with wrong error message\n')
            fail_count += 1
    except Exception:
        print('test 2 failed with worng error raised\n')
        fail_count += 1

    return fail_count


def error_test3():
    '''
    name: error_test3
    parameter: none
    return: number of failed cases for ValueError(plaintext) in encrypt()
    '''
    fail_count = 0
    try:
        pt3 = 'abcd1998'
        key3 = 'abcd'
        encrypt(pt3, key3)
        print('failed because it did not raise the error\n')
        fail_count += 1
    except ValueError as ex:
        if str(ex) == 'all characters in plaintext should be alphabet':
            print('error test 3 passed\n')
        else:
            print('test 3 failed with wrong error message\n')
            fail_count += 1
    except Exception:
        print('test 3 failed with wrong error raised\n')
        fail_count += 1

    return fail_count


def error_test4():
    '''
    name: error_tests
    parameter: none
    return: number of failed cases for TypeError(key) in decrypt()
    '''
    fail_count = 0
    try:
        ct4 = 'abcd'
        key4 = ['hello']
        decrypt(ct4, key4)
        print('failed because it did not raise the error\n')
        fail_count += 1
    except TypeError as ex:
        if str(ex) == 'key should be a string':
            print('error test 4 passed\n')
        else:
            print('test 4 failed with wrong error message\n')
            fail_count += 1
    except Exception:
        print('test 4 failed with worng error raised\n')
        fail_count += 1

    return fail_count


def error_test5():
    '''
    name: error_test5
    parameter: none
    return: number of failed cases for TypeError(ciphertext) in decrypt()
    '''
    fail_count = 0
    try:
        ct5 = 1234
        key5 = 'abcd'
        decrypt(ct5, key5)
        print('failed because it did not raise the error\n')
        fail_count += 1
    except TypeError as ex:
        if str(ex) == 'ciphertext should be a string':
            print('error test 5 passed\n')
        else:
            print('test 5 failed with wrong error message\n')
            print('actual message is:', ex)
            fail_count += 1
    except Exception:
        print('test 5 failed with worng error raised\n')
        fail_count += 1

    return fail_count


def error_test6():
    '''
    name: error_test6
    parameter: none
    return: number of failed cases for ValueError(ciphertext) in decrypt()
    '''
    fail_count = 0
    try:
        ct6 = 'abcd1998'
        key6 = 'xyzabg'
        decrypt(ct6, key6)
        print('failed because it did not raise the error\n')
        fail_count += 1
    except ValueError as ex:
        if str(ex) == 'all characters in ciphertext should be alphabet':
            print('error test 6 passed\n')
        else:
            print('test 6 failed with wrong error message\n')
            fail_count += 1
    except Exception:
        print('test 6 failed with wrong error raised\n')
        fail_count += 1

    return fail_count


def error_test7():
    '''
    name: error_test7
    parameter: none
    return: number of failed cases for ValueError(ciphertext) in decrypt()
    '''
    fail_count = 0
    try:
        ct7 = 'abcde'
        key7 = 'xyz'
        decrypt(ct7, key7)
        print('failed because it did not raise the error\n')
        fail_count += 1
    except ValueError as ex:
        if str(ex) == 'Ciphertext should have even number of letters':
            print('error test 7 passed\n')
        else:
            print('test 7 failed with wrong error message\n')
            fail_count += 1
    except Exception:
        print('test 7 failed with wrong error raised\n')
        fail_count += 1

    return fail_count


def error_test7():
    '''
    name: error_test8
    parameter: none
    return: number of failed cases for ValueError(ciphertext) in decrypt()
    '''
    fail_count = 0
    try:
        ct7 = 'abcdej'
        key7 = 'xyz'
        decrypt(ct7, key7)
        print('failed because it did not raise the error\n')
        fail_count += 1
    except ValueError as ex:
        if str(ex) == 'Ciphertext should not contain letter J':
            print('error test 7 passed\n')
        else:
            print('test 7 failed with wrong error message\n')
            fail_count += 1
    except Exception:
        print('test 7 failed with wrong error raised\n')
        fail_count += 1

    return fail_count


def main():
    failure = (run_tests_encrypt() + run_tests_decrypt() + error_test1()
               + error_test2() + error_test3() + error_test4() + error_test5()
               + error_test6() + error_test7())

    if failure == 0:
        print('Everything passed, yay!!!')
    else:
        print('Something went wrong, please fix!')


if __name__ == '__main__':
    main()
