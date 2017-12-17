from importlib import import_module
import os
import sys
from typing import List
from inspect import isclass, isfunction
from plugin import Plugin


def load_plugins(path):
    files = os.listdir(path)
    fullpath = os.path.join(os.getcwd(), path)

    if fullpath not in sys.path:
        sys.path.append(fullpath)

    return [import_module(f[:-3]) for f in files if f.endswith('.py')], [subc() for subc in Plugin.__subclasses__()]


loaded_modules, classes = load_plugins(path='plugins')
print(*classes, *loaded_modules, sep='\n')
