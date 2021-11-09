from pathlib import Path
from os import rename

RISK_OF_RAIN_2_INSTALL_PATH = Path(r'D:\programs\steam\steamapps\common\Risk of Rain 2').absolute()
DOORSTOP_FILE_NAME = 'doorstop_config.ini'
DISABLED_DOORSTOP_FILE_NAME = f'DISABLED_{DOORSTOP_FILE_NAME}'
HAS_DOORSTOP_FILE = (
        (RISK_OF_RAIN_2_INSTALL_PATH / DOORSTOP_FILE_NAME).exists()
        or (RISK_OF_RAIN_2_INSTALL_PATH / DISABLED_DOORSTOP_FILE_NAME).exists()
)

if not HAS_DOORSTOP_FILE:
    print(f'this risk of rain 2 install is not modded! "{DOORSTOP_FILE_NAME}" or "{DISABLED_DOORSTOP_FILE_NAME}" file does not exist.')
elif (path := (RISK_OF_RAIN_2_INSTALL_PATH / DOORSTOP_FILE_NAME)).exists():
    rename(path, RISK_OF_RAIN_2_INSTALL_PATH / DISABLED_DOORSTOP_FILE_NAME)
    print('risk of rain 2 mods have been DISABLED')
elif (path := (RISK_OF_RAIN_2_INSTALL_PATH / DISABLED_DOORSTOP_FILE_NAME)).exists():
    rename(path, RISK_OF_RAIN_2_INSTALL_PATH / DOORSTOP_FILE_NAME)
    print('risk of rain 2 mods have been ENABLED')

input('\n(press enter to exit script...)')
