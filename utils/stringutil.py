from typing import Union, Callable, List, Tuple, Set


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


def auto_str_filtered(is_valid):
    if isinstance(is_valid, (list, tuple, set)):
        if any(map(callable, is_valid)):
            is_valid_filter = lambda attribute: \
                any(((callable(item) and item(attribute))
                     or (isinstance(item, (list, set, tuple)) and attribute in item)
                     or item == attribute)
                    for item in is_valid)
        else:
            is_valid_filter = is_valid.__contains__

    elif callable(is_valid):
        is_valid_filter = is_valid
    else:
        is_valid_filter = is_valid

    def _auto_str_inner(cls):
        def __str__(self):
            pairs = ' '.join(
                f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_') and is_valid_filter(k))
            return f'<{self.__class__.__name__} {pairs}>'

        cls.__str__ = __str__
        return cls

    return _auto_str_inner
