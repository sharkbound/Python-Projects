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

def encrypt_step(string, step=10):
    enc_str = ''
    for i, c in enumerate(string):
        new_char = chr(ord(c) + i + step)
        enc_str += new_char
    return enc_str


def decrypt_step(string, step=10):
    enc_str = ''
    for i, c in enumerate(string):
        new_char = chr(ord(c) - i - step)
        enc_str += new_char
    return enc_str


'''
NOTES:
    step 10,000+ start producing arrows question marks and strange charaters
    step 100,000 blocks

'''
def encrypt_key(string, key, step=0):
    while len(key) < len(string):
        key *= 2

    enc_str = ''
    for i, c in enumerate(string):
        new_char = chr(ord(c) + ord(key[i]) % 256 + step)
        enc_str += new_char
    return enc_str


def decrypt_key(string, key, step=0):
    while len(key) < len(string):
        key *= 2

    enc_str = ''
    for i, c in enumerate(string):
        new_char = chr(ord(c) - ord(key[i]) % 256 - step)
        enc_str += new_char
    return enc_str
