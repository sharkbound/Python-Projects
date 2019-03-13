# requirements

you have have the pypi package "twine" and "wheel" installed

```
pip install twine --upgrade
pip install wheel --upgrade
```


# building the package

to build the package, make a `setup.py` file, then do the following 

(if you are on windows, use `py` else use `python3`)

```
py setup.py sdist bdist_wheel
```

once built, it will generate a .tar and .whl file in `dist` folder

now we can upload it


# uploading


to upload, we use twine, make sure to clean any older whl and tar files from the dist folder before doing this step:
(if you are on windows, use `py` else use `python3`)

```
py -m twine upload dist/*
```

it will ask for your pypi username/password, after that you are done


# testing uploading to pypi

pypi has a test server you can use, it is `https://test.pypi.org/legacy/`
(note, pypi test server is separate from the main index server, so you need to create a separate account for it at https://test.pypi.org)

to use this test server add `--repository-url https://test.pypi.org/legacy/` after `upload` example:

```
py -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```