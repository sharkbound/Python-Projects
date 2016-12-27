@echo off

echo -------------------------------------
echo Setting Directory to script's Directory...
cd %~dp0
echo Set active Directory to: %cd%
echo -------------------------------------

echo -------------------------------------
echo Trying to run setup.py....
echo -------------------------------------
setup.py install


echo -------------------------------------
echo NOTE:
echo This does not isntall pygame, you must install it separately!
echo -------------------------------------

pause