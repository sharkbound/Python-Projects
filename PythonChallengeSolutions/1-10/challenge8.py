import ast

import requests
import re
import bz2


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
    req = requests.get(url)
    matches = re.findall(r'\'.*\'', req.text)

    user = eval(f'b{matches[0]}')
    password =  eval(f'b{matches[1]}')

    print(bz2.decompress(user).decode('utf-8'),
          '\n',bz2.decompress(password).decode('utf-8'))