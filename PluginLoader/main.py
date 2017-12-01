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

    modules = [import_module(f[:-3]) for f in files if f.endswith('.py')]
    plugin_instances = []

    for m in modules:
        for k,v in m.__dict__.items():
            if isclass(v) and v is not Plugin:
                inst = v()
                if isinstance(inst, Plugin):
                    plugin_instances.append(inst)

    return modules, plugin_instances


loaded_modules, classes = load_plugins(path='plugins')
print(classes)
# for k, v in loaded_modules[0].__dict__.items():
#     if isclass(v):
