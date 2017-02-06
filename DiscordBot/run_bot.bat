@echo off
echo ================= Upgrading / installing dependencies =================
echo.
pip3 install discord.py --user --upgrade
echo.
echo ================================= Done ================================
echo.
echo Starting bot...
echo.
python Main.py
pause
exit

