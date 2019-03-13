from setuptools import setup, find_packages

with open('readme.md') as file:
    description = file.read()

setup(
    name='package-name',
    version='0.0.1',
    description='my first pypi package',
    long_description=description,
    long_description_content_type='text/markdown',
    author='john doe',
    url='typically a link to the projects github page, ex: github.com/johndoe',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ],
)
