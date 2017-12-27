from importlib import import_module
import os
import sys
from inspect import isclass, isfunction
from modulefinder import Module
from plugin import Plugin


class PluginInfo:
    def __init__(self, module: Module, plugin, cls):
        self.module = module
        self.plugin = plugin
        self.cls = cls

    name = property(lambda self: self.plugin.name)
    commands = property(lambda self: self.plugin.commands)


def load_plugins(cls, path, *init_args, **init_kwargs):
    files = os.listdir(path)
    fullpath = os.path.join(os.getcwd(), path)

    if fullpath not in sys.path:
        sys.path.append(fullpath)

    loaded_modules = [import_module(f[:-3]) for f in files if f.endswith('.py')]
    subclasses = []
    for module in loaded_modules:
        for _, v in module.__dict__.items():
            if isclass(v) and v is not cls and cls in v.__mro__:
                yield PluginInfo(module, v(*init_args, **init_kwargs), v)

for p in load_plugins(Plugin, 'plugins'):
    print(p.name, p.commands, p.plugin, p.module, p.cls, sep='\n')
