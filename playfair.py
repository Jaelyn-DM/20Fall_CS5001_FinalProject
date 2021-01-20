'''
Duo Ma (Jaelyn)
CS 5001 Fall 2020
HW#8 Playfair Cipher
This program implement encryption and decryption of Playfair Cipher
'''


from utils import strip
from utils import standard_format
from utils import validate_string_1 as validate_plaintext
from utils import validate_string_2 as validate_ciphertext
from utils import validate_string_3 as validate_key


def encrypt(plaintext, key):
    '''
    name: encrypt()
    parameter: key: a string keyword (letters only); plaintext that to be
    encoded by playfair cipher
    return: ciphertext (string) transfered from plaintext by playfair cipher
    '''

    # validate plaintext
    validate_plaintext(plaintext)

    # validate key
    validate_key(key)
    key = standard_format(key)

    # build key_square matrix
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    original = key + alphabet
    encoded = ''
    for letters in original:
        if letters == 'J':
            letters = 'I'
        if letters not in encoded:
            encoded += letters

    key_square = {}
    for letters in encoded:
        i = encoded.index(letters)
        x = (i // 5) + 1
        y = (i % 5) + 1
        key_square[letters] = (x, y)

    key_square_2 = {}
    for pair in key_square:
        key_square_2[key_square[pair]] = pair

    # replace 2nd occurance with 'X' for any double letters
    plaintext = strip(plaintext).upper()

    # make the plaintext an even number of letters
    if len(plaintext) % 2 == 1:
        plaintext += 'X'

    # locating letters in key_square:
    ciphertext = ''
    i = 0
    while i < len(plaintext):
        x = plaintext[i]
        if x == 'J':
            x = 'I'
        y = plaintext[i + 1]
        if y == 'J':
            y = 'I'
        if y == x:
            y = 'X'

        # rule 1 if two letters are on the same row:
        if key_square[x][0] == key_square[y][0]:
            row = key_square[x][0]
            column_x = key_square[x][1] + 1
            if column_x == 6:
                column_x = 1
            column_y = key_square[y][1] + 1
            if column_y == 6:
                column_y = 1
            new_x = key_square_2[(row, column_x)]
            new_y = key_square_2[(row, column_y)]
            ciphertext += new_x + new_y
        # rule 2 if two letters are on the same column:
        elif key_square[x][1] == key_square[y][1]:
            column = key_square[x][1]
            row_x = key_square[x][0] + 1
            if row_x == 6:
                row_x = 1
            row_y = key_square[y][0] + 1
            if row_y == 6:
                row_y = 1
            new_x = key_square_2[(row_x, column)]
            new_y = key_square_2[(row_y, column)]
            ciphertext += new_x + new_y
        # rule 3 if two letters are not on same row nor same column
        else:
            row_x = key_square[x][0]
            column_x = key_square[y][1]
            row_y = key_square[y][0]
            column_y = key_square[x][1]
            new_x = key_square_2[(row_x, column_x)]
            new_y = key_square_2[(row_y, column_y)]
            ciphertext += new_x + new_y
        i += 2

    return ciphertext


def decrypt(ciphertext, key):
    '''
    name: decrypt
    parameter: ciphertext(string that needs to be decrypted by playfair);
    key(string)
    return: plaintext that is decrypted from the input ciphertext
    '''

    # validate ciphertext
    validate_ciphertext(ciphertext)
    if len(ciphertext) % 2 != 0:
        raise ValueError('Ciphertext should have even number of letters')
    ciphertext = standard_format(ciphertext)
    for letter in ciphertext:
        if letter == 'J':
            raise ValueError('Ciphertext should not contain letter J')

    # validate key
    validate_key(key)
    key = standard_format(key)

    # build key_square matrix
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    original = strip(key).upper() + alphabet
    encoded = ''
    for letters in original:
        if letters == 'J':
            letters = 'I'
        if letters not in encoded:
            encoded += letters

    key_square = {}
    for letters in encoded:
        i = encoded.index(letters)
        x = (i // 5) + 1
        y = (i % 5) + 1
        key_square[letters] = (x, y)

    key_square_2 = {}
    for pair in key_square:
        key_square_2[key_square[pair]] = pair

    # locating letters in key_square:
    plaintext = ''
    i = 0
    while i < len(ciphertext):
        x = ciphertext[i]
        y = ciphertext[i + 1]
        # if two letters are on the same row:
        if key_square[x][0] == key_square[y][0]:
            row = key_square[x][0]
            column_x = key_square[x][1] - 1
            if column_x == 0:
                column_x = 5
            column_y = key_square[y][1] - 1
            if column_y == 0:
                column_y = 5
            new_x = key_square_2[(row, column_x)]
            new_y = key_square_2[(row, column_y)]
            plaintext += new_x + new_y
        # if two letters are on the same column:
        elif key_square[x][1] == key_square[y][1]:
            column = key_square[x][1]
            row_x = key_square[x][0] - 1
            if row_x == 0:
                row_x = 5
            row_y = key_square[y][0] - 1
            if row_y == 0:
                row_y = 5
            new_x = key_square_2[(row_x, column)]
            new_y = key_square_2[(row_y, column)]
            plaintext += new_x + new_y
        # if two letters are not on same row nor same column
        else:
            row_x = key_square[x][0]
            column_x = key_square[y][1]
            row_y = key_square[y][0]
            column_y = key_square[x][1]
            new_x = key_square_2[(row_x, column_x)]
            new_y = key_square_2[(row_y, column_y)]
            plaintext += new_x + new_y
        i += 2

    return plaintext
