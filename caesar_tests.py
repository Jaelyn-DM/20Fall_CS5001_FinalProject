'''
Duo Ma
CS5001 Fall 2020
Homework#8 Ciphers Part 1
this is a program to test if the caesar cipher program works fine
'''


from caesar import encrypt
from caesar import decrypt


def test_encrypt(plaintext, key, expected):
    '''
    name: test_encrypt
    parameter: plaintext (string), key(an integer), another string(expected
    ciphertext returned from the encrypt function)
    return: boolean value: True if expected matches the actual, False otherwise
    '''
    actual = encrypt(plaintext, key)

    return actual == expected


def run_tests_encrypt():
    '''
    name: run_tests_encrypt()
    parameter: none
    return an integer: number of failed test cases
    '''
    print('\nstart testing encrypt fucntion for Caesar cipher\n')
    fail_count = 0
    # test 1
    if test_encrypt('Prof Jump is crazy to think we can do this', 3,
                    'SURIMXPSLVFUDCBWRWKLQNZHFDQGRWKLV'):
        print('test 1 passed\n')
    else:
        print('test 1 failed\n')
        fail_count += 1

    # test 2
    x = 'hello my name is Jaelyn'
    y = 'mjqqtrdsfrjnxofjqds'.upper()
    if test_encrypt(x, 5, y):
        print('test 2 passed\n')
    else:
        print('test 2 failed\n')
        fail_count += 1

    # test 3
    x = 'hey! how are you?'
    y = 'fcwfmuypcwms'.upper()
    if test_encrypt(x, 24, y):
        print('test 3 passed\n')
    else:
        print('test 3 failed\n')
        fail_count += 1

    # test 4
    x = 'hey! how are you?'
    y = 'fcwfmuypcwms'.upper()
    if test_encrypt(x, -2, y):
        print('test 4 passed\n')
    else:
        print('test 4 failed\n')
        fail_count += 1

    # test 5
    x = 'heyhowareyou'
    y = x.upper()
    if test_encrypt(x, 0, y):
        print('test 5 passed\n')
    else:
        print('test 5 failed\n')
        fail_count += 1

    # test 6
    x = 'helloworld!!!'
    y = 'dahhksknhz'.upper()
    if test_encrypt(x, 100, y):
        print('test 6 passed\n')
    else:
        print('test 6 failed\n')
        fail_count += 1

    # test 7
    x = 'helloworld!'
    y = 'lippsasvph'.upper()
    if test_encrypt(x, -100, y):
        print('test 7 passed\n')
    else:
        print('test 7 failed\n')
        fail_count += 1

    return fail_count


def test_decrypt(ciphertext, key, expected):
    '''
    name: test_decrypt
    parameter: ciphertext (string), key(an integer), another string(expected
    plaintext returned from the decrypt function)
    return: boolean value: True if expected matches the actual, False otherwise
    '''
    actual = decrypt(ciphertext, key)

    return actual == expected


def run_tests_decrypt():
    '''
    name: run_tests_decrypt()
    parameter: none
    return an integer: number of failed test cases
    '''
    print('\nstart testing decrypt fucntion for Caesar cipher\n')
    fail_count = 0

    # test 1
    x = 'SURIMXPSLVFUDCBWRWKLQNZHFDQGRWKLV'
    y = 'ProfJumpiscrazytothinkwecandothis'.upper()
    if test_decrypt(x, 3, y):
        print('test 1 passed\n')
    else:
        print('test 1 failed\n')
        fail_count += 1

    # test 2
    x = 'iujwiaeofwahuj'.upper()
    y = 'mynameisjaelyn'.upper()
    if test_decrypt(x, 22, y):
        print('test 2 passed\n')
    else:
        print('test 2 failed\n')
        fail_count += 1

    # test 3
    x = 'pmofkdfpzljfkd'.upper()
    y = 'springiscoming'.upper()
    if test_decrypt(x, -3, y):
        print('test 3 passed\n')
    else:
        print('test 3 failed\n')
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
        key3 = 1
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
            print('actual message is:', ex)
            fail_count += 1
    except Exception:
        print('test 2 failed with worng error raised\n')
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


def main():
    failure = (run_tests_encrypt() + run_tests_decrypt() + error_test1() +
               error_test2() + error_test3() + error_test4() + error_test5()
               + error_test6())
    if failure == 0:
        print('\nAll tests passed! Yayy')
    else:
        print('\nSomething went wrong, please fix!')


if __name__ == '__main__':
    main()
