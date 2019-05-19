def _get_indent(s: str):
    return len(s) - len(s.lstrip())


def trim_indent(string: str):
    lines = string.splitlines(keepends=False)
    min_indent = min(map(_get_indent, lines))
    return '\n'.join(line[min_indent:] for line in lines)


def trim_margin(string: str, margin: str = '|'):
    return '\n'.join(
        line[line.index(margin) + 1:]
        if margin in line
        else line
        for line in string.splitlines()
    )
