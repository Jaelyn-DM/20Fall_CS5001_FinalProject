'''
Duo Ma (Jaelyn)
CS5001 Fall 2020
HW9 Ciphers part 2
this program is to implement the encrypt function and decryption functioni in
Beale Cipher method
'''

import random
import string
import os
from utils import validate_string_1 as validate_plaintext
from utils import validate_string_2 as validate_ciphertext
from utils import validate_int
from utils import standard_format
from utils import transfer_to_int
from utils import open_file


def encrypt(plaintext, key_filename, key_seed):
    '''
    name: encrypt(); this function will encrypt valid plaintext to ciphertext
    via Beale cipher methods...
    parameter: plaintext: a string message that needs to be encrypted;
    key_filename: is the name of the file that contains the key text; key_seed:
    the integer to generate random integers(index)
    return: ciphertext that encrypted from the plaintext
    '''
    # validate plaintext
    plaintext = validate_plaintext(plaintext)
    plaintext = standard_format(plaintext)

    # validate key_seed (integer)
    key_seed = validate_int(key_seed)

    # open file and read filedata, validate key_filename
    filedata = open_file(key_filename)

    # index all words in the filedata
    all_words = ['#placehoder']
    for lines in filedata:
        for letters in lines:
            if letters in string.punctuation:
                lines = lines.replace(letters, '')
        lines = lines.split(' ')
        for words in lines:
            if words != '' and words != '\n':
                all_words.append(words)

    # build dictionay of letter:indexes
    word_index = dict()
    i = 0
    while i < len(all_words):
        if all_words[i][0].isalpha():
            x = all_words[i][0]
            y = all_words[i][0].upper()
            all_words[i] = all_words[i].replace(x, y)
            if all_words[i][0] not in word_index.keys():
                word_index[all_words[i][0]] = [i]
            else:
                word_index[all_words[i][0]].append(i)
        i += 1

    # transfer plaintext to ciphertext by generating random key
    letter_cipher = []
    for letter in plaintext:
        if letter not in word_index.keys():
            raise ValueError('Key file does not have enough words')
        elif len(word_index[letter]) == 0:
            raise ValueError('Key file does not have enough words')
        else:
            random.seed(key_seed)
            x = random.choice(word_index[letter])
            letter_cipher.append(x)
            word_index[letter].remove(x)
    ciphertext = ' '.join(map(str, letter_cipher))

    return ciphertext


def decrypt(ciphertext, key_filename):
    '''
    name: decrypt(); this function will decrypt valid ciphertext to plaintext
    via Beale cipher methods...
    parameter: ciphertext: a string message that needs to be decrypted;
    key_filename: is the name of the file that contains the key text; key_seed:
    the integer to generate random integers(index)
    return: plaintext that decrypted from the ciphertext
    '''
    # validate ciphertext
    if not isinstance(ciphertext, str):
        raise TypeError('ciphertext should be a string')
    if len(ciphertext) == 0:
        raise ValueError('ciphertext should have at least 1 letter')
    cipher_code = ciphertext.split()
    for code in cipher_code:
        if not code.isdigit():
            raise ValueError('ciphertext should contains numbers only')

    # open file and read filedata, validate key_filename
    filedata = open_file(key_filename)

    # index all words in the filedata
    all_words = ['#placehoder']
    for lines in filedata:
        for letters in lines:
            if letters in string.punctuation:
                lines = lines.replace(letters, '')
        lines = lines.split(' ')
        for words in lines:
            if words != '' and words != '\n':
                all_words.append(words)

    # transfer ciphertext to plaintext by generating random key
    plaintext = ''
    for code in cipher_code:
        if int(code) >= len(all_words):
            raise ValueError('Key does not have enough words')
        plaintext += all_words[int(code)][0].upper()

    return plaintext
