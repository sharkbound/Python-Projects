import re


def split_iter(string: str, *delimiters: str):
    delimiters = '|'.join(delimiters or ('\r\n', '\n', '\r'))
    yield from (m[0] for m in re.finditer(rf'([^{delimiters}]+)', string))


def _get_indent(s: str):
    return len(s) - len(s.lstrip())


def trim_indent(string: str):
    lines = string.splitlines(keepends=False)
    min_indent = min(map(_get_indent, lines))
    return '\n'.join(line[min_indent:] for line in lines)


def trim_margin(string: str, margin: str = '|'):
    print(*split_iter(string))
    return '\n'.join(line[line.index(margin) + 1:] if margin in line else line for line in split_iter(string))


# print(trim_indent(
#     '''\
#     hello
#     world!
#     i
#     love
#     you'''
# ))

print(trim_margin('''\
     |  |hi
  |hello'''))
