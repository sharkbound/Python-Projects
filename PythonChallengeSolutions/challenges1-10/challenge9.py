import re
import requests

# user: huge
# pass: file
if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/return/good.html:huge:file'
    text = ''
    with open('../files/challenge9.html') as f:
        text = f.read().replace('\n', '')

    first_text = re.findall('first:\s*[0-9,]*', text)
    second_text = re.findall('second:\s*[0-9,]*', text)

    print(first_text)
    print(second_text)
