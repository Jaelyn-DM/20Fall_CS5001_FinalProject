'''
Duo Ma (Jaelyn)
CS5001 Fall 2020
Homework#9 Ciphers Part-2
Substitution Cipher - this is a program that can implement substitution cipher
'''


from utils import strip
from utils import standard_format
from utils import validate_string_1 as validate_plaintext
from utils import validate_string_2 as validate_ciphertext
from utils import validate_string_4 as validate_alphakey


def encrypt(plaintext, key):
    '''
    name: encrypt() in substitution cipher method
    parameter: a string that is the plaintext that needs to be encoded,
    jumbled alphabet ofall 26 letters (string) as a key
    return: a ciphertext string that returned from encoding plaintext
    by substitution method.
    '''

    # to validate key and adjust format
    key = validate_alphakey(key)

    # to ensure the plaintext is valid(string)
    validate_plaintext(plaintext)

    # to adjust format of plaintext
    plaintext = standard_format(plaintext)

    # to match from plaintext to ciphertext
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ''
    for letter in plaintext:
        ciphertext += key[alphabet.index(letter)]

    return ciphertext


def decrypt(ciphertext, key):
    '''
    name: decrypt() in substitution cipher method
    parameter: a string that is the ciphertext that needs to be encoded,
    jumbled alphabet of all 26 letters (string) as a key
    return: a plaintext string that returned from the ciphertext decrypted
    by substitution method.
    '''

    # to validate key and adjust format
    key = validate_alphakey(key)

    # to ensure the cipher is valid(string)
    validate_ciphertext(ciphertext)
    # to adjust format of ciphertext
    ciphertext = standard_format(ciphertext)

    # to match from ciphertext to plaintext
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = ''
    for letter in ciphertext:
        plaintext += alphabet[key.index(letter)]

    return plaintext
