import importlib.abc
import json
import sys
import types
from importlib.abc import Loader
from importlib.machinery import ModuleSpec
from importlib.util import spec_from_file_location
from os import PathLike
from pathlib import Path
from types import ModuleType
from typing import Optional, Sequence


class JsonModuleLoader(Loader):
    def exec_module(self, module: ModuleType) -> None:
        with open(module.__spec__.origin) as json_in:
            json_data = json.load(json_in)

            def get(name, default=None):
                return json_data.get(name, default)

            module._raw_json = json_data
            for name, value in json_data.items():
                if name.isidentifier():
                    setattr(module, name, value)

            module.get = get


class JsonMetaPathFinder(importlib.abc.MetaPathFinder):
    def find_spec(self,
                  fullname: str,
                  path: Optional[Sequence[PathLike]],
                  target: Optional[types.ModuleType] = ...) -> Optional[ModuleSpec]:
        if not path:
            paths = [Path.cwd()]
        else:
            paths = [Path(string) for string in path]

        for path in paths:
            for file in path.iterdir():
                if file.name.endswith('.json') and file.name.split('.')[-2] == fullname.split('.')[-1]:
                    return spec_from_file_location(name=fullname, location=file.absolute(), loader=JsonModuleLoader())


sys.meta_path.append(JsonMetaPathFinder())

