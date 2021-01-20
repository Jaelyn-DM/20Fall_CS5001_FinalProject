'''
Duo Ma (Jaelyn)
CS5001 Fall 2020
Homework#8 Ciphers Part-1
this file contaisn all the helper functions
that are helpful to multiple ciphers
'''


import string


def strip(words):
    '''
    name: strip
    parameter: string
    return: input string but without all the punctuations and spaces
    '''
    # strip the punctuation out
    for c in words:
        if c in string.punctuation:
            words = words.replace(c, '')

    # strip the space out
    return words.replace(' ', '')


def standard_format(text):
    '''
    name: standard_format
    parameter: text (string)
    return:text that are stripped and with uppercase letters only
    '''
    output = strip(text).upper()
    return output


def validate_string_1(text):
    '''
    name: validate_string_1 (for plaintext only)
    parameter: string (has at least 1 letter, contains letters only)
    return: raise error if parameter is not a valid string
    '''
    # to validate plaintext
    if not isinstance(text, str):
        raise TypeError('plaintext should be a string')
    elif len(text) == 0:
        raise ValueError('plaintext should have at least 1 letter')
    text = strip(text)
    if not text.isalpha():
        raise ValueError('all characters in plaintext should be alphabet')


def validate_string_2(text):
    '''
    name: validate_string_2 (for ciphertext only)
    parameter: string (has at least 1 letter, contains letters only)
    return: raise error if parameter is not a valid string
    '''
    # to validate ciphertext
    if not isinstance(text, str):
        raise TypeError('ciphertext should be a string')
    if len(text) == 0:
        raise ValueError('ciphertext should have at least 1 letter')
    text = strip(text)
    if not text.isalpha():
        raise ValueError('all characters in ciphertext should be alphabet')


def validate_string_3(text):
    '''
    name: validate_string_3 (for keys only in playfair)
    parameter: key(string)
    return: raise error if parameter is not a valid string
    '''
    if not isinstance(text, str):
        raise TypeError('key should be a string')
    text = strip(text)
    if not text.isalpha():
        raise ValueError('all characters in key should be alphabet')


def validate_int(num):
    '''
    name: validate_int (for keys)
    parameter: an integer
    return: raise error if parameter is not an integer
    '''
    if not isinstance(num, int):
        raise TypeError('Key should be an integer')
