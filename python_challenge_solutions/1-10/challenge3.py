import os
import sys
import webbrowser
import re
import requests
import time

src_txt_file = '../textfiles/challenge3.txt'
output_txt = '../output_txt/challenge3.txt'


def write_source_code_text_to_file():
    req_result = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')

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


def entry():
    write_source_code_text_to_file()
    text = get_jumbled_text_from_source()
    text = text.replace('\n', '', text.count('\n'))

    matches = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text)

    anwser = "".join(matches)
    print(anwser)

    # print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", text)))


if __name__ == '__main__':
    entry()
