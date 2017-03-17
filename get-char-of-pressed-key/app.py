import os, sys
from msvcrt import getch


def start():
    while True:
        raw_key_value = getch()
        key_int_value = ord(raw_key_value)
        key_char_value = chr(key_int_value)
        print(f'pressed key \n'
              f'Raw Value: {raw_key_value}\nInt value: {key_int_value}\nKey char: {key_char_value}')


if __name__ == '__main__':
    start()
