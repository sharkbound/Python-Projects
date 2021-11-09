import os
import sys
import importlib

def load_extensions(folder_path):
    if not os.path.isabs(folder_path):
        folder_path = os.path.abspath(folder_path)

    if folder_path not in sys.path:
        sys.path.append(folder_path)

    for file in os.listdir(folder_path):
        file_name, ext = os.path.splitext(file)
        if not ext == '.py': continue

        module = importlib.import_module(file_name)
        if 'setup' in module.__dict__:
            module.setup()

