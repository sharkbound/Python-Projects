import sys
import os

import re
import requests

base_nothing_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
nothing_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'



def extract_nothing_number(url):
    r = requests.get(url)
    try:
        return re.findall(r'is (\d+)', r.text)[-1]
    except:
        return r.text


def entry():
    next_nothing = 0
    for x in range(400):
        # if type(next_nothing) != 'int' and x != 0:
        #     break

        if x == 0:
            next_nothing = extract_nothing_number(base_nothing_url)
        else:
            next_nothing = extract_nothing_number(nothing_url.format(next_nothing))

        print(next_nothing, f"LOOP-{x}")
        # print(nothing_url.format(next_nothing))

    print(next_nothing)



if __name__ == '__main__':
    entry()
