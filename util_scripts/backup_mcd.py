import shutil
from pathlib import Path
import os
from datetime import datetime

GAME_SAVE = Path(os.getenv('APPDATA'), '../local/dungeons').absolute()
WORKING = Path().absolute()
NOW = datetime.now()
BACKUP = Path('backups/').absolute() / f'{NOW.year}_{NOW.month}_{NOW.day}__{NOW.hour}_{NOW.minute}'
#
# if not BACKUP.exists():
#     BACKUP.mkdir(parents=True)

shutil.copytree(GAME_SAVE, BACKUP)
