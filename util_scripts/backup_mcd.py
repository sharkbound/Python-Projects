import shutil
from pathlib import Path
import os
from datetime import datetime

GAME_SAVE = Path(os.getenv('APPDATA'), '../local/dungeons').absolute()
WORKING = Path().absolute()
NOW = datetime.now()
BACKUP = Path('backups/').absolute() / f'{NOW.day}_{NOW.month}_{NOW.year}__{NOW.minute}_{NOW.hour}'

shutil.copytree(GAME_SAVE, BACKUP)
