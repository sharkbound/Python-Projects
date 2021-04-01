import re

from icecream import ic

RE_VAR = re.compile(r'(?P<name>[*\w]+):?(?P<hint>[\[\],\'\"\w\d]+)?=?(?P<default>[()\[\]\-+,\'\"\d\w]+)?')


def tabs(count):
    return '    ' * count


CANNOT_BE_NONE = object()
CAN_BE_NONE = object()


def run_once():
    output = []

    if classname := input('enter class name: ').strip():
        output.append(f'class {classname}')

    if superclass := input('enter superclass [leave blank for none]: ').strip():
        output.append(f'({superclass}):\n{tabs(1)}')
    else:
        output.append(f':\n{tabs(1)}')

    output.append('def __init__(self, ')
    all_vars = []
    while match := RE_VAR.match(input('enter variable: ').strip().replace(' ', '')):
        groups = match.groupdict()
        all_vars.append(groups['name'])
        seen = set()
        for key, formatter in (
                ('name', lambda g, seen: g['name']),
                ('hint', lambda g, seen: f': {g["hint"]}'),
                ('default', lambda g, seen: f' = {g["default"]}' if 'hint' in seen else f'={g["default"]}'),
        ):
            if groups[key] is None:
                continue

            seen.add(key)
            output.append(formatter(groups, seen))

        output.append(', ')

    output.pop()
    output.append(f'):')

    for var in all_vars:
        var = var.replace('*', '')
        output.append(f'\n{tabs(2)}self.{var} = {var}')

    # output[-1] = output[-1].rstrip()
    return ''.join(output)


while True:
    out = run_once()

    print('\nfinal class:\n\n')
    print(out)
    print('\n\n')

    if input('copy output to clipboard? [Y/(N)]').lower().strip() == 'y':
        import pyperclip

        pyperclip.copy(out)

    if input('\n\ngo again? [(Y)/N]: ').strip().lower() == 'n':
        break
