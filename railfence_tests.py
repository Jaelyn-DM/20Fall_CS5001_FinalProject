'''
Duo Ma (Jaelyn)
CS5001 Fall 2020
Homework#8 Cipher Part-1
Rail Fence Cipher tests: this program to test if  Rail Fence Cipher works fine
'''

from railfence import encrypt
from railfence import decrypt


def test_encrypt(plaintext, key, expected):
    '''
    name: test_encrpt
    parameter: plaintext(string: text that needs to be encoded, letters only);
    key: an integer; exepcted string returned after encrypting
    return: True if actual matches the expected, False otherwise
    '''
    actual = encrypt(plaintext, key)
    return actual == expected


def run_tests_encrypt():
    '''
    name: run_tests_encrypt
    parameter: none
    return: number of failed test cases of railfence encryption
    '''
    print('\nStart testing Rail Fence Encrypt...')
    fail_count = 0

    # test 1
    pt1 = 'helloworld'
    ct1 = 'holelwrdlo'.upper()
    if test_encrypt(pt1, 3, ct1):
        print('test 1 passed')
    else:
        print('test 1 failed')
        fail_count += 1

    # test 2
    pt2 = 'Prof Jump is crazy to think we can do this...'
    ct2 = 'PMAHCHRUPRZTIEATIOJICYONWNOSFSTKD'
    if test_encrypt(pt2, 4, ct2):
        print('test 2 passed')
    else:
        print('test 2 failed')
        fail_count += 1

    # test 3
    pt3 = 'what is your name?'
    ct3 = 'waiyunmhtsorae'.upper()
    if test_encrypt(pt3, 2, ct3):
        print('test 3 passed')
    else:
        print('test 3 failed')
        fail_count += 1

    # test 4
    pt4 = "I'm an aligner in Northeastern"
    ct4 = 'iemhaatsnrtaoelnrinnginre'.upper()
    if test_encrypt(pt4, 10, ct4):
        print('test 4 passed')
    else:
        print('test 4 failed')
        fail_count += 1

    # test 5
    pt5 = 'SOS'
    ct5 = 'SOS'
    if test_encrypt(pt5, 3, ct5):
        print('test 5 passed')
    else:
        print('test 5 failed')
        fail_count += 1

    # test 6
    pt6 = 'northeasternaligner'
    ct6 = 'northeasternaligner'.upper()
    if test_encrypt(pt6, 19, ct6):
        print('test 6 passed')
    else:
        print('test 6 failed')
        fail_count += 1

    return fail_count


def test_decrypt(ciphertext, key, expected):
    '''
    name: test_decrypt
    parameter: ciphertext: encoded text (string) by rail fence ciphers; key: an
    integer; expected plaintext decrypted by rail fence ciphers(string)
    return: True if actual matches the expected, False otherwise
    '''
    actual = decrypt(ciphertext, key)
    return actual == expected


def run_tests_decrypt():
    '''
    name: run_tests_decrypt()
    parameter: none
    return: number of failed test cases
    '''
    print('\nStart testing Rail Fence decrypt...')
    fail_count = 0

    # test 1
    ct1 = 'PMAHCHRUPRZTIEATIOJICYONWNOSFSTKD'
    pt1 = 'ProfJumpiscrazytothinkwecandothis'.upper()
    if test_decrypt(ct1, 4, pt1):
        print('test 1 passed')
    else:
        print('test 1 failed')
        fail_count += 1

    # test 2
    ct2 = 'hloolelwrd'
    pt2 = 'helloworld'.upper()
    if test_decrypt(ct2, 2, pt2):
        print('test 2 passed')
    else:
        print('test 2 failed')
        fail_count += 1

    # test 3
    ct3 = 'nnogerirtlhaenarset'
    pt3 = 'northeasternaligner'.upper()
    if test_decrypt(ct3, 9, pt3):
        print('test 3 passed')
    else:
        print('test 3 failed')
        fail_count += 1

    # test 4
    ct4 = 'northeasternaligner'
    pt4 = 'northeasternaligner'.upper()
    if test_decrypt(ct4, 19, pt4):
        print('test 4 passed')
    else:
        print('test 4 failed')
        fail_count += 1

    # test 5
    ct5 = 'bguseoienvovoalsyrrsiiacelnenwkajnrgep'
    pt5 = 'BeijingVancouverLosAngelesNewYorkParis'.upper()
    if test_decrypt(ct5, 4, pt5):
        print('test 5 passed')
    else:
        print('test 5 failed')
        fail_count += 1

    # test 6
    ct6 = 'evvasrsigauesnenokijnnorogleypriclewa'
    pt6 = 'eijingVancouverLosAngelesNewYorkParis'.upper()
    if test_decrypt(ct6, 4, pt6):
        print('test 6 passed')
    else:
        print('test 6 failed')
        fail_count += 1

    # test 7
    ct7 = 'iaennkjvnvragserpsigculseewoainoolyr'
    pt7 = 'ijingVancouverLosAngelesNewYorkParis'.upper()
    if test_decrypt(ct7, 4, pt7):
        print('test 7 passed')
    else:
        print('test 7 failed')
        fail_count += 1

    # test 8
    ct8 = 'jnrgepiacelnenwkanvovoalsyrrsguseoi'
    pt8 = 'jingVancouverLosAngelesNewYorkParis'.upper()
    if test_decrypt(ct8, 4, pt8):
        print('test 8 passed')
    else:
        print('test 8 failed')
        fail_count += 1

    # test 9
    ct9 = 'iclewannorogleyprgauesnenokivvasrs'
    pt9 = 'ingVancouverLosAngelesNewYorkParis'.upper()
    if test_decrypt(ct9, 4, pt9):
        print('test 9 passed')
    else:
        print('test 9 failed')
        fail_count += 1

    # test 10
    ct10 = 'noolyrgculseewoaivnvragserpsaennk'
    pt10 = 'ngVancouverLosAngelesNewYorkParis'.upper()
    if test_decrypt(ct10, 4, pt10):
        print('test 10 passed')
    else:
        print('test 10 failed')
        fail_count += 1

    # test 11
    ct11 = 'guseoivovoalsyrrsacelnenwkanrgep'
    pt11 = 'gVancouverLosAngelesNewYorkParis'.upper()
    if test_decrypt(ct11, 4, pt11):
        print('test 11 passed')
    else:
        print('test 11 failed')
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
        key1 = 'aaa'
        encrypt(pt1, key1)
        print('failed because it did not raise the error\n')
        fail_count += 1
    except TypeError as ex:
        if str(ex) == 'Numeric key should be an integer':
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
        pt2 = [1, 2, 3]
        key2 = 2
        encrypt(pt2, key2)
        print('failed because it did not raise the error\n')
        fail_count += 1
    except TypeError as ex:
        if str(ex) == 'plaintext should be a string':
            print('error test 2 passed\n')
        else:
            print('test 2 failed with wrong error message\n')
            print(ex)
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
        key3 = 1
        encrypt(pt3, key3)
        print('failed because it did not raise the error\n')
        fail_count += 1
    except ValueError as ex:
        if str(ex) == 'all characters in plaintext should be alphabet':
            print('error test 3 passed\n')
        else:
            print('test 3 failed, wrong error message\n')
            print(ex)
            fail_count += 1
    except Exception:
        print('test 3 failed, wrong error raised\n')
        fail_count += 1

    return fail_count


def error_test4():
    '''
    name: error_test4
    parameter: none
    return: number of failed cases for TypeError(key) in decrypt()
    '''
    fail_count = 0
    try:
        ct1 = 'abcd'
        key1 = 'aaa'
        decrypt(ct1, key1)
        print('failed because it did not raise the error\n')
        fail_count += 1
    except TypeError as ex:
        if str(ex) == 'Numeric key should be an integer':
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
        ct2 = 1234
        key2 = 2
        decrypt(ct2, key2)
        print('failed because it did not raise the error\n')
        fail_count += 1
    except TypeError as ex:
        if str(ex) == 'ciphertext should be a string':
            print('error test 5 passed\n')
        else:
            print('test 5 failed with wrong error message\n')
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
        ct3 = 'abcd1998'
        key3 = 1
        decrypt(ct3, key3)
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
        ct3 = 'abcdefg'
        key3 = 1
        decrypt(ct3, key3)
        print('failed, it did not raise the error\n')
        fail_count += 1
    except ValueError as ex:
        if str(ex) == 'key should be at least 2':
            print('error test 7 passed\n')
        else:
            print('test 7 failed, wrong error message\n')
            fail_count += 1
    except Exception:
        print('test 7 failed, wrong error raised\n')
        fail_count += 1

    return fail_count


def main():
    failure = (run_tests_encrypt() + run_tests_decrypt() + error_test1() +
               error_test2() + error_test3() + error_test4() + error_test5()
               + error_test6() + error_test7())
    if failure == 0:
        print('\nALL tests passed! Yay!\n')
    else:
        print('\nSomething went wrong, please fix...\n')


if __name__ == '__main__':
    main()
