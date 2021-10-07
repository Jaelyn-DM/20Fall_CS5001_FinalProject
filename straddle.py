'''
Duo Ma (Jaelyn)
CS 5001 Fall 2020
HW#9 Cipher Part2
This program implement encryption and decryption of Straddle Checkboard Cipher
'''

from utils import strip
from utils import standard_format
from utils import validate_string_1 as validate_plaintext
from utils import validate_string_2 as validate_ciphertext
from utils import validate_string_4 as validate_alphakey
from utils import validate_int


def encrypt(plaintext, key_word, key_num, key_adder):
    '''
    function name: encrypt(), this is the function that encrypt a plaintext to
    ciphertext by straddle cipher
    parameters: plaintext: string, message to be encrypted; key_word = full 26
    alphabet in any order; key_num = two distinct number between 1 and 9;
    key_adder: positive integer of any length
    return: ciphertext encrypted from the plaintext by straddle cipher
    '''
    # validate plaintext, and make it in standard format
    plaintext = validate_plaintext(plaintext)
    plaintext = standard_format(plaintext)

    # validate key_word
    key_word = validate_alphakey(key_word)

    # validate key_num, verify two distinct numbers
    key_num = validate_int(key_num)
    if key_num < 10 or key_num > 99:
        raise ValueError('Numeric key should contain two digit')
    a = key_num // 10
    b = key_num % 10
    if a == 0 or b == 0:
        raise ValueError('Numbers in numeric key should be greater than zero')
    elif a == b:
        raise ValueError('Two numbers in numeric key should be distinct')
    elif a > b:
        key_num_x = b
        key_num_y = a
    elif b > a:
        key_num_x = a
        key_num_y = b

    # validate key_adder
    key_adder = validate_int(key_adder)
    if key_adder <= 0:
        raise ValueError('a valid adder should be a positive integer')
    elif len(str(key_adder)) == 0:
        raise ValueError('key_adder should have at least one digit')

    # build dictionary of encoded alphabet:index
    key_matrix = {}

    # give indexes for letters on row_0
    row_0 = key_word[:8]
    count = 0
    for i in range(0, 10):
        if i == key_num_x or i == key_num_y:
            count += 1
        elif count == 0:
            key_matrix[row_0[i]] = i
        elif count == 1:
            key_matrix[row_0[i - 1]] = i
        elif count == 2:
            key_matrix[row_0[i - 2]] = i

    # give indexes for letters on row_x
    row_x = key_word[8:18]
    x = key_num_x * 10
    for i in range(0, 10):
        key_matrix[row_x[i]] = x + i

    # give indexes for letters on row_z
    row_y = key_word[18:]
    y = key_num_y * 10
    for i in range(0, 8):
        key_matrix[row_y[i]] = y + i
    key_matrix['0'] = y + 8
    key_matrix['1'] = y + 9

    # transfer plaintext to num_text by locating index of each letter
    num_text = ''
    for letter in plaintext:
        num_code = key_matrix[letter]
        num_text += str(num_code)

    # transfer num_text to adder_text by adding key_adder to each digit
    cycle = len(str(key_adder))
    adder_text = ''
    i = 0
    while i < len(num_text):
        position = i % cycle
        adder_code = int(num_text[i]) + int(str(key_adder)[position])
        if adder_code > 9:
            adder_code = adder_code % 10
        adder_text += str(adder_code)
        i += 1

    # build another dictionary of encoded index:alphabet
    another_matrix = {}
    for letter in key_matrix:
        another_matrix[key_matrix[letter]] = letter

    # transfer the adder_text to ciphertext
    ciphertext = ''
    i = 0
    while i < len(adder_text):
        if int(adder_text[i]) == key_num_x or int(adder_text[i]) == key_num_y:
            if len(adder_text) == 1:
                i = 1
            else:
                letter_code = int(adder_text[0:2])
                ciphertext += another_matrix[letter_code]
                adder_text = adder_text[2:]
        else:
            letter_code = int(adder_text[0])
            ciphertext += another_matrix[letter_code]
            adder_text = adder_text[1:]

    # adjust format and return ciphertext
    ciphertext = standard_format(ciphertext)

    return ciphertext


def decrypt(ciphertext, key_word, key_num, key_adder):
    '''
    function name: decrypt(), this is the function that decrypt a ciphertext to
    plaintext by straddle cipher
    parameters: ciphertext: string, message to be encrypted; key_word = full 26
    alphabet in any order; key_num = two distinct number between 1 and 9;
    key_adder: positive integer of any length
    return: plaintext decrypted from the ciphertext by straddle cipher
    '''

    # validate ciphertext, and make it in standard format
    if not isinstance(ciphertext, str):
        raise TypeError('ciphertext should be a string')
    if len(ciphertext) == 0:
        raise ValueError('ciphertext should have at least 1 letter')
    ciphertext = standard_format(ciphertext)
    for letter in ciphertext:
        if letter != '0' and letter != '1' and not letter.isalpha():
            raise ValueError('all characters in ciphertext should be alphabet')

    # validate key_word
    key_word = validate_alphakey(key_word)
    key_word = standard_format(key_word)

    # validate key_num, verify two distinct numbers
    key_num = validate_int(key_num)
    if key_num < 10 or key_num > 99:
        raise ValueError('Numeric key should contain two digit')
    a = key_num // 10
    b = key_num % 10
    if a == 0 or b == 0:
        raise ValueError('Numbers in numeric key should be greater than zero')
    elif a == b:
        raise ValueError('Two numbers in numeric key should be distinct')
    elif a > b:
        key_num_x = b
        key_num_y = a
    elif b > a:
        key_num_x = a
        key_num_y = b

    # validate key_adder
    key_adder = validate_int(key_adder)
    if key_adder <= 0:
        raise ValueError('a valid adder should be a positive integer')
    elif len(str(key_adder)) == 0:
        raise ValueError('key_adder should have at leat one digit')

    # build dictionary of encoded alphabet:index
    key_matrix = {}

    # give indexes for letters on row_0
    row_0 = key_word[:8]
    count = 0
    for i in range(0, 10):
        if i == key_num_x or i == key_num_y:
            count += 1
        elif count == 0:
            key_matrix[row_0[i]] = i
        elif count == 1:
            key_matrix[row_0[i - 1]] = i
        elif count == 2:
            key_matrix[row_0[i - 2]] = i

    # give indexes for letters on row_x
    row_x = key_word[8:18]
    x = key_num_x * 10
    for i in range(0, 10):
        key_matrix[row_x[i]] = x + i

    # give indexes for letters on row_z
    row_y = key_word[18:]
    y = key_num_y * 10
    for i in range(0, 8):
        key_matrix[row_y[i]] = y + i
    key_matrix['0'] = y + 8
    key_matrix['1'] = y + 9

    # build another dictionary of encoded index:alphabet
    another_matrix = {}
    for letter in key_matrix:
        another_matrix[key_matrix[letter]] = letter

    # transfer ciphertext to adder_text by locating index of each letter
    adder_text = ''
    for letter in ciphertext:
        adder_code = key_matrix[letter]
        adder_text += str(adder_code)

    # transfer adder_text to num_text by substracting key_adder from each digit
    cycle = len(str(key_adder))
    num_text = ''
    i = 0
    while i < len(adder_text):
        position = i % cycle
        num_code = int(adder_text[i]) - int(str(key_adder)[position])
        if num_code < 0:
            num_code = int(adder_text[i]) + 10 - int(str(key_adder)[position])
        num_text += str(num_code)
        i += 1

    # transfer the num_text to plainrtext
    plaintext = ''
    i = 0
    while i < len(num_text):
        if int(num_text[i]) == key_num_x or int(num_text[i]) == key_num_y:
            if len(num_text) == 1:
                i = 1
            else:
                letter_code = int(num_text[0:2])
                plaintext += another_matrix[letter_code]
                num_text = num_text[2:]
        else:
            letter_code = int(num_text[0])
            plaintext += another_matrix[letter_code]
            num_text = num_text[1:]

    # adjust format and return plaintext
    plaintext = standard_format(plaintext)

    return plaintext
