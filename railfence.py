'''
Duo Ma (Jaelyn)
CS5001 Fall 2020
Homework#8 Cipher Part-1
Rail Fence Cipher: this program implement an approach of encryption called
Rail Fence Cipher
'''


from utils import strip
from utils import standard_format
from utils import validate_string_1 as validate_plaintext
from utils import validate_string_2 as validate_ciphertext
from utils import validate_int as validate_key


def encrypt(plaintext, key):
    '''
    name: encrypt()
    parameter: plaintext-string texts that needs to be encoded, letters
    only; key-an integer value
    return: ciphertext transformed from plaintext by rail fence encrytion
    '''
    # validate plaintext
    validate_plaintext(plaintext)
    plaintext = standard_format(plaintext)

    # validate key
    validate_key(key)
    if key < 2:
        raise ValueError('key should be at least 2')
    if key > len(plaintext):
        print('You might want to use a different key... this one is too big')

    # calculate number of rails
    end = 2
    middle = key - 2
    group = end + middle * 2

    # build a dict including a group of rails (end rails + middle rails*2)
    group_dict = {}
    for i in range(1, group + 1):
        group_dict[i] = []

    # place letters in rails (middle rails are seperated to two parts)
    r = 1
    for letter in plaintext:
        group_dict[r].append(letter)
        if r < group:
            r += 1
        elif r == group:
            r = 1

    # combine the two seperated middle rails into one
    if key > 2:
        mid_dict = {}
        for i in range(1, middle + 1):
            mid_dict[i] = ''
            for letter in group_dict[i + 1]:
                mid_dict[i] += letter + ' '
            x = 0
            while x < len(group_dict[group + 1 - i]):
                y = group_dict[group + 1 - i][x]
                mid_dict[i] = mid_dict[i].replace(' ', y, 1)
                x += 1
            mid_dict[i] = strip(mid_dict[i])

    # print out ciphertext
    start_rail = ''
    for letter in group_dict[1]:
        start_rail += letter
    end_rail = ''
    for letter in group_dict[key]:
        end_rail += letter
    mid_rails = ''
    for i in range(1, middle + 1):
        mid_rails += mid_dict[i]
    ciphertext = start_rail + mid_rails + end_rail

    return ciphertext


def decrypt(ciphertext, key):
    '''
    name: encrypt()
    parameter: ciphertext transformed from plaintext by rail fence
    encrytion, letters only; key-an integer value
    return: plaintext decrypted from ciphertext by rail fence encrytion
    '''

    # validate ciphertext
    validate_ciphertext(ciphertext)
    ciphertext = standard_format(ciphertext)

    # validate key
    validate_key(key)
    if key < 2:
        raise ValueError('key should be at least 2')
    if key > len(ciphertext):
        print('You might want to use a different key... this one is too big')

    group = (key - 2) * 2 + 2
    n = len(ciphertext) // group
    # to calculate how many letters in each rail
    rails = {}
    for i in range(1, key + 1):
        if i == 1 or i == key:
            rails[i] = n
        else:
            rails[i] = 2 * n
    rest = len(ciphertext) % group
    if rest > 0 and rest <= key:
        i = 1
        while i <= rest:
            rails[i] += 1
            i += 1
    elif rest > key:
        i = 1
        while i <= rest:
            if i <= key:
                rails[i] += 1
            else:
                x = key - (i - key)
                rails[x] += 1
            i += 1

    # to build dictionay rails of texts
    ct = ciphertext
    rail_text = {}
    for i in range(1, key + 1):
        rail_text[i] = ct[:rails[i]]
        ct = ct.replace(ct[:rails[i]], '', 1)

    plaintext = ''
    # rotate n number of groups
    for num in range(n):
        # matching plaintext within each group
        i = 1
        while i <= group:
            if i <= key and len(rail_text[i]) > 0:
                plaintext += rail_text[i][0]
                rail_text[i] = rail_text[i].replace(rail_text[i][0], '', 1)
            elif i > key:
                x = 2 * key - i
                if len(rail_text[x]) > 0:
                    plaintext += rail_text[x][0]
                    rail_text[x] = rail_text[x].replace(rail_text[x][0], '', 1)
            i += 1

    # matching plaintext outside of a complete group
    i = 1
    while i <= rest:
        if i <= key and len(rail_text[i]) > 0:
            plaintext += rail_text[i][0]
            rail_text[i] = rail_text[i].replace(rail_text[i][0], '', 1)
        elif i > key:
            x = 2 * key - i
            if len(rail_text[x]) > 0:
                plaintext += rail_text[x][0]
                rail_text[x] = rail_text[x].replace(rail_text[x][0], '', 1)
        i += 1

    return plaintext
