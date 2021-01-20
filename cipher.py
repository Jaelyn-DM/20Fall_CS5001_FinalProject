'''
Duo Ma (Jaelyn)
CS 5001 Fall 2020
HW8 Ciphers - Part1
this program implements the main functions and other organizing codes
'''

from utils import strip
from caesar import encrypt as caesar_encrypt
from caesar import decrypt as caesar_decrypt
from railfence import encrypt as railfence_encrypt
from railfence import decrypt as railfence_decrypt
from playfair import encrypt as playfair_encrypt
from playfair import decrypt as playfair_decrypt


def main():
    try:
        # ask user input of decrypt or encrypt
        to_do = str(input('Menu: \nEncrypt(E)\nDecrypt(D)\nQuit(Q)\n'))
        to_do = strip(to_do).upper()
        while to_do != 'Q':

            while to_do != 'E' and to_do != 'D' and to_do != 'Q':
                to_do = input('Menu: \nEncrypt(E)\nDecrypt(D)\nQuit(Q)\n')
                to_do = strip(to_do).upper()
            if to_do == 'Q':
                break

            # ask user input which cipher method to use
            cipher_type = input('which type of cipher would you like to use? \
        \nCaesar(C)\nRail Fence(R)\nPlayfair(P)\n')
            cipher_type = strip(cipher_type).upper()
            while (cipher_type != 'C' and cipher_type != 'R'
                   and cipher_type != 'P'):
                cipher_type = input('which type of cipher would you like to \
use? nCaesar(C)\nRailfence(R)\nPlayfair(P)\n')
                cipher_type = strip(cipher_type).upper()

            # perform cipher functions
            if to_do == 'E' and cipher_type == 'C':
                plaintext = input('what is the plaintext:\n')
                key = int(input('what is the key?\n'))
                ciphertext = caesar_encrypt(plaintext, key)
                print('\n\nEncryping plaintext', plaintext, 'using Caesar \
Cipher with key', key, 'will get ciphertext:', ciphertext, '\n\n')

            elif to_do == 'D' and cipher_type == 'C':
                ciphertext = input('what is the ciphertext:\n')
                key = int(input('what is the key?\n'))
                plaintext = caesar_decrypt(ciphertext, key)
                print('\n\nDecryping ciphertext', ciphertext, 'using Caesar \
Cipher with key', key, 'will get plaintext:', plaintext, '\n\n')

            elif to_do == 'E' and cipher_type == 'R':
                plaintext = input('what is the plaintext:\n')
                key = int(input('what is the key?\n'))
                ciphertext = railfence_encrypt(plaintext, key)
                print('\n\nEncryping plaintext', plaintext, 'using Rail \
Fence Cipher with key', key, 'will get ciphertext:', ciphertext, '\n\n')

            elif to_do == 'D' and cipher_type == 'R':
                ciphertext = input('what is the ciphertext:\n')
                key = int(input('what is the key?\n'))
                plaintext = railfence_decrypt(ciphertext, key)
                print('\n\nDecryping ciphertext', ciphertext, 'using Rail \
Fence Cipher with key', key, 'will get plaintext:', plaintext, '\n\n')

            elif to_do == 'E' and cipher_type == 'P':
                plaintext = input('what is the plaintext:\n')
                key = input('what is the key?\n')
                ciphertext = playfair_encrypt(plaintext, key)
                print('\n\nEncryping plaintext', plaintext, 'using Playfair \
Cipher with key', key, 'will get ciphertext:', ciphertext, '\n\n')
            elif to_do == 'D' and cipher_type == 'P':
                ciphertext = input('what is the ciphertext:\n')
                key = input('what is the key?\n')
                plaintext = playfair_decrypt(ciphertext, key)
                print('\n\nDecryping ciphertext', ciphertext, 'using Caesar \
Cipher with key', key, 'will get plaintext:', plaintext, '\n\n')

            to_do = ''

    except Exception as ex:
        print('Error found', str(ex))


if __name__ == '__main__':
    main()
