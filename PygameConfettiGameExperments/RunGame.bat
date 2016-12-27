@echo off

echo -------------------------------------
echo Setting Directory to script's Directory...
cd %~dp0
echo Set active Directory to: %cd%
echo -------------------------------------

echo ---------------------------------
echo PRESS ANY BUTTON TO EXIT THE GAME
echo ---------------------------------

echo ---------------------------------
echo Running Main.py...
echo ---------------------------------

Main.py

echo ---------------------------------
echo Game was closed...
echo ---------------------------------

pause