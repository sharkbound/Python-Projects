def _get_indent(s: str):
    return len(s) - len(s.lstrip())


def trim_indent(string: str):
    lines = [l for l in string.splitlines(keepends=False) if l.strip()]
    min_indent = min(map(_get_indent, lines))
    return '\n'.join(line[min_indent:] for line in lines)


def trim_margin(string: str, margin: str = '|'):
    return '\n'.join(
        line[line.index(margin) + 1:]
        if margin in line
        else line
        for line in string.splitlines()
    )


def auto_str(cls):
    def __str__(self):
        pairs = ' '.join(f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_'))
        return f'<{self.__class__.__name__} {pairs}>'

    cls.__str__ = __str__
    return cls
