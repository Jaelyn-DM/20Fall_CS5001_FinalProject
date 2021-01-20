'''
Duo Ma (Jaelyn)
CS5001 Fall 2020
Homework#8 Ciphers Part-1
Caesar Cipher - this is a progam that implements encryption and decryption of caesar cipher.
'''


from utils import strip
from utils import standard_format
from utils import validate_string_1 as validate_plaintext
from utils import validate_string_2 as validate_ciphertext
from utils import validate_int as validate_key


def encrypt(plaintext, key):
    '''
    name: encrypt
    parameter: a string that is the plaintext that needs to be encoded, an
    integer as a key
    return: a ciphertext string that returned from encoding plaintext
    by caesar cipher method.
    '''

    # to ensure key is valid (integer)
    validate_key(key)
    if key % 26 == 0:
        print('You might want to use another key though...')

    # to ensure the plaintext is valid(string)
    validate_plaintext(plaintext)

    # to adjust format of plaintext
    plaintext = standard_format(plaintext)

    # to calculate the position different from plaintext to ciphertext
    original = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    move_position = key % len(original)

    # to build the encoded alphabet
    encoded = ''
    encoded = encoded + original[move_position:] + original[:move_position]

    # to match from plaintext to ciphertext
    ciphertext = ''
    for letter in plaintext:
        ciphertext += encoded[original.index(letter)]

    return ciphertext


def decrypt(ciphertext, key):
    '''
    name: decrypt
    parameter: ciphertext(a string that is encoded by Caesar cipher) and
    a key(an integer)
    return: plaintext (a string that is decrypted by Caesar cipher
    from the ciphertect)
    '''

    # to ensure key is an integer(positive or negative)
    validate_key(key)

    # to ensure the plaintext contains letters only
    validate_ciphertext(ciphertext)

    # to adjust format of the ciphertext
    ciphertext = standard_format(ciphertext)

    # to calculate the position difference between ciphertext and plaintext
    original = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    move_position = key % len(original)

    # to build the encoded alphabet
    encoded = ''
    encoded = encoded + original[move_position:] + original[:move_position]

    # to match from ciphertext to plaintext
    plaintext = ''
    for letters in ciphertext:
        plaintext += original[encoded.index(letters)]

    return plaintext
