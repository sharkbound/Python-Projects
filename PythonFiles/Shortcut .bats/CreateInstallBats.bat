@echo off

set /P depName=Enter Package name to generate install .bats for:  
set NLM=^


set NL=^^^%NLM%%NLM%^%NLM%%NLM%

echo pip install %depName% %NL% pause > ..\DepInstallScripts\AdminDepInstalls\Install_%depName%.bat
echo pip install --user %depName% %NL% pause > ..\DepInstallScripts\UserDepInstalls\Install_%depName%.bat