from json import load, dump
import re
from argparse import ArgumentParser

# FILE = r'C:\Users\owner\Desktop\classes.json'
# OUT = r'C:\Users\owner\Desktop\out.json'

RE_LINE = re.compile(r'\*+?([^*]+)\*+?\s*([^*]+)')


def find_contents(data, parent, key):
    if isinstance(data, dict):
        for k, v in data.items():
            yield from find_contents(v, data, k)

    elif isinstance(data, list) and key == 'content' and all(isinstance(x, str) for x in data):
        yield data, parent, key
 

def list_to_dict(data):
    def _replace(m):
        return '_' if m[0].isspace() else ''

    out = {}
    other = []
    for line in data:
        matches = RE_LINE.findall(line)
        if not matches:
            other.append(line)
            continue

        for key, value in matches:
            key = re.sub(r'\s|\W', _replace, key).strip('_').lower()
            out[key] = value.strip('\n, ')

    out['other'] = other
    return out


def replace_content(json):
    for data, parent, key in find_contents(json, json, ''):
        parent[key] = list_to_dict(data)

    return json


def main():
    parser = ArgumentParser()
    parser.add_argument('-i', help='input character JSON file', required=True)
    parser.add_argument('-o', help='file to output the fixed character JSON to', required=True)
    args = parser.parse_args()

    with open(args.i, encoding='UTF8') as read_file, open(args.o, 'w') as write_file:
        dump(replace_content(load(read_file)), write_file, indent=4)


if __name__ == '__main__':
    main()
