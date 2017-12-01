import zipfile
import requests
import os
import shutil

# location of the unturned instances managed folder
MANAGED_FOLDER = r'REMOVED'
UNTURNED_DLL_NAMES = ['Assembly-CSharp.dll', 'Assembly-CSharp-firstpass.dll', 'UnityEngine.dll']
ROCKET_ZIP_LINK = 'https://ci.rocketmod.net/job/Rocket.Unturned/lastSuccessfulBuild/artifact/Rocket.Unturned/bin/Release/Rocket.zip'
ROCKET_DLL_NAMES = ['Rocket.API.dll', 'Rocket.Core.dll', 'Rocket.Unturned.dll']
ZIP_FILE_NAME = 'Rocket.zip'
LIB_FOLDER_NAME = 'lib'

if not os.path.exists(ZIP_FILE_NAME):
    with open(ZIP_FILE_NAME, 'wb') as destination:
        shutil.copyfileobj(requests.get(ROCKET_ZIP_LINK, stream=True).raw, destination)

if not os.path.exists(LIB_FOLDER_NAME):
    os.mkdir(LIB_FOLDER_NAME)

rocketzip = zipfile.ZipFile(ZIP_FILE_NAME)
for fname in ROCKET_DLL_NAMES:
    for file in rocketzip.filelist:
        if file.filename.endswith(fname):
            rocketzip.extract(file, LIB_FOLDER_NAME)
            shutil.move(f'{LIB_FOLDER_NAME}/Modules/Rocket.Unturned/{fname}', LIB_FOLDER_NAME)

for fname in UNTURNED_DLL_NAMES:
    shutil.copy(os.path.join(MANAGED_FOLDER, fname), LIB_FOLDER_NAME)

shutil.rmtree(os.path.join(os.getcwd(), LIB_FOLDER_NAME, 'Modules'))
