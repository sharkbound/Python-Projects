import warnings

import helper
import re

GET_KEY_VALUE_RE = re.compile(r'(\w+)\s?=\s?(.+)')
ASSIGNMENT_RE = re.compile(r'.+=.+')
STR_ASSIGNMENT_RE = re.compile(r'(\w+)\s?=\s?"(.+)"')

def parse(fname) -> dict:
    dct = {}
    for l in helper.read_file_lines(fname):
        if ASSIGNMENT_RE.match(l):
            key,value = map(str.strip, GET_KEY_VALUE_RE.findall(l)[0])

            iv = parse_to_int(value)
            if iv[0]:
                dct[key] = iv[1]
            elif '"' in value:
                dct[key] = value.strip('"')
    return dct

def parse_to_int(value):
    try:
        return (True, int(value))
    except:
        return (False, None)