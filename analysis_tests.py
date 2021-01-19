'''
Duo Ma (Jaelyn)
CS5001 2020 Fall
HW7 Statistics
this is a test suite for the main program
'''

from analysis import read_data
from analysis import average
from analysis import std_dev
from statistics import stdev


def test_average(num_list, expected):
    '''
    name: test_average()
    parameter: a list of numbers, a float of expected average result of the
    input list of numbers
    return: boolean value (True if actual result == expected, False otherwise)
    '''
    actual = average(num_list)
    return actual == expected


def run_tests_average():
    '''
    name: run_tests_average()
    parameter: None
    return: int: number of failed test cases for average()
    '''
    print('\nStart testing function average()')
    fail_count = 0

    # test 1
    num_list_1 = [1, 1, 1, 1, 1]
    expected_1 = 1.0
    if test_average(num_list_1, expected_1):
        print('test 1 passed!')
    else:
        print('test 1 failed')
        fail_cout += 1

    # test 2
    num_list_2 = [10, 20, 30, 40]
    expected_2 = 25.0
    if test_average(num_list_2, expected_2):
        print('test 2 passed!')
    else:
        print('test 2 failed')
        fail_count += 1

    # test 3
    num_list_3 = [-10, 0, 10, 20, 30]
    expected_3 = 10.0
    if test_average(num_list_3, expected_3):
        print('test 3 passed!')
    else:
        print('test 3 failed')
        fail_count += 1

    # test 4
    num_list_4 = [10.5, 20.5, 30.5, 40.5]
    expected_4 = 25.5
    if test_average(num_list_4, expected_4):
        print('test 4 passed!')
    else:
        print('test 4 failed')
        fail_count += 1

    # test 5
    num_list_5 = [-10.2, -20.2, -30.2, -40.2]
    expected_5 = -25.2
    if test_average(num_list_5, expected_5):
        print('test 5 passed!')
    else:
        print('test 5 failed')
        fail_countr += 1

    return fail_count


def test_std_dev(num_list, expected):
    '''
    name: test_std_dev(), to test if std_dev function words as expected
    parameter: num_list(a list of numbers); expected: a float of expected
    result as the standard deviation of the numbers in the list
    return: boolean value (True if actual result matches the expected, False
    otherwise)
    '''
    actual = std_dev(num_list)
    return actual == expected


def run_tests_std_dev():
    '''
    name: run_test_std_dev()
    parameter: none
    result: number of failed test cases for std_dev()
    '''
    print('\nStart testing function std_dev()')
    fail_count = 0

    # test 1
    num_list_1 = [1, 1, 1, 1, 1]
    expected_1 = 0.0
    if test_std_dev(num_list_1, expected_1):
        print('test 1 passed!')
    else:
        print('test 1 failed')
        fail_count += 1

    # test 2
    num_list_2 = [10, 20, 30, 40]
    expected_2 = stdev(num_list_2)
    if test_std_dev(num_list_2, expected_2):
        print('test 2 passed')
    else:
        print('test 2 failed')
        fail_count += 1

    # test 3
    num_list_3 = [10, 100, 1000, 10000]
    expected_3 = stdev(num_list_3)
    if test_std_dev(num_list_3, expected_3):
        print('test 3 passed')
    else:
        print('test 3 failed')
        fail_count += 1

    # test 4
    num_list_4 = [-30, 0, 60, 90, 80]
    expected_4 = stdev(num_list_4)
    if test_std_dev(num_list_4, expected_4):
        print('test 4 passed')
    else:
        print('test 4 failed')
        fail_count += 1

    # test 5
    num_list_5 = [100.9, 34.5, 56.8, 88.6]
    expected_5 = stdev(num_list_5)
    if test_std_dev(num_list_5, expected_5):
        print('test 5 passed')
    else:
        print('test 5 failed')
        fail_count += 1

    # test 6
    num_list_6 = [-100.9, -23.5, -6.8, -38.4]
    expected_6 = stdev(num_list_6)
    if test_std_dev(num_list_6, expected_6):
        print('test 6 passed')
    else:
        print('test 6 failed')
        fail_count += 1

    return fail_count


def main():
    failure = run_tests_average() + run_tests_std_dev()
    if failure == 0:
        print('\nALL PASSED!')
    else:
        print('\nSomething went wrong, please fix!')


if __name__ == '__main__':
    main()
