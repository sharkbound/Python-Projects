import re
from functools import partial

from utils.stringutil import trim_indent


def generate_scheme_ascii_art(*lines, filler='.'):
    """
    example output:
    (list (display (quote _o_)) (display (quote __o)) (display (quote ooo)) (display (quote glider)) (display (quote btw)))
    """
    if len(lines) == 1 and isinstance(lines[0], str):
        lines = lines[0].splitlines()

    mid = ' '.join(
        f'(display (quote {line}))'
        for line in
        map(partial(re.sub, r'[\\ "]', filler), lines)
        if line.strip()
    )
    return f'(list {mid})'


print(generate_scheme_ascii_art(trim_indent(
    r'''\
    
    '''
)))
