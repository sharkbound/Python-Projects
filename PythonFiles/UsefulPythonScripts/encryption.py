import base64

from string import ascii_letters


def encode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return encoded_string  # base64.urlsafe_b64encode(encoded_string)


def decode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) - ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return encoded_string  # base64.urlsafe_b64encode(encoded_string)


def encrypt(string, step=10):
    enc_str = ''
    for i, c in enumerate(string):
        new_char = chr(ord(c) + i + step)
        enc_str += new_char
    return enc_str


def decrypt(string, step=10):
    enc_str = ''
    for i, c in enumerate(string):
        new_char = chr(ord(c) - i - step)
        enc_str += new_char
    return enc_str


def encrypt_key(string, key, step=0):
    key = key * len(string)
    enc_str = ''
    for i, c in enumerate(string):
        new_char = chr(ord(c) + ord(key[i]) + step)
        enc_str += new_char
    return enc_str


def decrypt_key(string, key, step=0):
    key = key * len(string)
    enc_str = ''
    for i, c in enumerate(string):
        new_char = chr(ord(c) - ord(key[i]) - step)
        enc_str += new_char
    return enc_str
