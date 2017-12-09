from data.config import Config
import os


def create_config():
    return Config('config.json', foldername='Config', username='BOT_NAME', oauth='oauth: OAUTH', nick='NICK_NAME',
                  channel='CHANNEL')


def reset():
    global cfg
    os.remove(cfg.abs_path)
    cfg = create_config()


cfg = create_config()
