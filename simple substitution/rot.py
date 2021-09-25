import sys
import string

while True:
    mod = input('press e for encrypt or d for decrypt: ').lower()
    if mod == 'e' or mod == 'd':
        break
    print('bad input')

if mod == 'e':
    msg = input('message to encrypt: ')
    rot = input('number of rotation (default 13): ') or 13
    cryptogram = ''
    for i, letter in enumerate(msg):
        if letter not in string.ascii_lowercase:
            cryptogram += new_letter
            continue
        upper = letter.isupper()
        letter.lower()
        index = string.ascii_lowercase.index(letter)
        new_index = (index + rot) % 26
        new_letter = string.ascii_lowercase[new_index]
        cryptogram += new_letter
    
    print(f'cryptograph: {cryptogram}')

if mod == 'd':
    cryptogram = input('cryptogram: ')
    rot = input('number of rotation (default 13): ') or 13
    msg = ''
    for i, letter in enumerate(cryptogram):
        if letter not in string.ascii_lowercase:
            msg += new_letter
            continue
        upper = letter.isupper()
        letter.lower()
        index = string.ascii_lowercase.index(letter)
        new_index = (index - rot) % 26
        new_letter = string.ascii_lowercase[new_index]
        msg += new_letter

    print(f'message: {msg}')