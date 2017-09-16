import os
from enum import Enum
from pathlib import Path

import data


class Mode(Enum):
    ENCRYPT, DECRYPT = range(2)


def main():
    while True:
        option = main_menu()

        if option == '1':
            crypto_menu(Mode.ENCRYPT)
        elif option == '2':
            crypto_menu(Mode.DECRYPT)
        elif option in 'Qq':
            quit()


def main_menu():
    return get_input('Choose a option:\n\t1) encrypt text\n\t2) decrypt text\n\n\tQ) Quit', *'12Qq')


def crypto_menu(mode):
    if mode == Mode.ENCRYPT:
        r = get_input('Choose a option:\n\t1) Encrypt text from a file\n\t2) Encrypt text from console', *'12')
    else:
        r = get_input('Choose a option:\n\t1) Decrypt text from a file\n\t2) Decrypt text from console', *'12')

    if r == '1':
        try:
            with open(input('Enter file name: '), 'r') as f:
                text = data.encrypt(*f.read()) if mode == Mode.ENCRYPT else data.decrypt(f.read())
        except FileNotFoundError as e:
            print(e)
    elif r == '2':
        if mode == Mode.ENCRYPT:
            text = data.encrypt(*input('Enter text to encrypt:\n').replace(r'\n', '\n'))
        else:
            text = data.decrypt(input('Enter text to decrypt:\n'))

    fname = input('Enter output file name: ')
    with open(fname, 'w') as f:
        f.write(text)
        msg = f'Saved to {fname}'
        print(f'\n{"="*len(msg)}\n{msg}\n{"="*len(msg)}')


def get_input(prompt, *valid_responses):
    r = None
    while r not in valid_responses:
        r = input(prompt + '\n\nSelection: ')
    return r


if __name__ == '__main__':
    main()
