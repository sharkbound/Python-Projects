import os
import sys
import requests
from collections import defaultdict

src_txt_file = '../textfiles/challenge2.txt'
output_txt = '../output_txt/challenge2.txt'


def write_source_code_text_to_file():
    req_result = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')

    with open(src_txt_file, 'w') as file:
        file.write(req_result.text)


def get_jumbled_text_from_source():
    write_source_code_text_to_file()

    file = open(src_txt_file)
    text = file.read()

    jumbled_start_index = text.rfind('<!--') + 4
    jumbled_end_index = text.rfind('-->')

    sub_string = text[jumbled_start_index:jumbled_end_index]

    with open(output_txt, 'w') as f:
        f.write(sub_string)

    file.close()
    return sub_string


def get_char_count(input_string):
    char_c = defaultdict(int)
    for c in input_string:
        char_c[c] += 1

    return char_c


def entry():
    text = get_jumbled_text_from_source()
    chars = get_char_count(text)
    filtered = [k for k,v in chars.items() if v == 1]
    final = ''.join(filtered)

    print(final)


if __name__ == '__main__':
    entry()
