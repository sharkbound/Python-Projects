import subprocess

subprocess.call(['cythonize', '-i', '-a', r'cdefs\*.pyx'])
