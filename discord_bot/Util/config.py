import json
import os

config_path_complete = "Config\\bot_config.json"
config_filename = "bot_config.json"
config_folder_name = "Config"


class BotConfig:
    def __init__(self):
        self.config_path_complete = "Config\\bot_config.json"
        self.config_filename = "bot_config.json"
        self.config_folder_name = "Config"
        self._create_default_config()

        self.config_data = self.get_config_values()
        self.connection_info = self.config_data['ConnectionInfo']
        self.settings = self.config_data['Settings']
        self.command_prefix = self.settings['commandprefix']
        self.token = self.connection_info['Token']
        self.owner_id = self.settings['OwnerID']

    def _create_default_config(self):
        json_str = json.dumps(self._get_default_settings(), indent="\t")

        if not os.path.exists(config_path_complete):
            if not os.path.exists("Config"):
                os.mkdir("Config")
            if not os.path.exists(config_path_complete):
                with open(f"{config_folder_name}\\{config_filename}", "w") as config_file:
                    config_file.write(json_str)

    def _get_default_settings(self):
        default = {}
        default['ConnectionInfo'] = {
            'OwnerID': 'change me',
            'Token': 1111111111111
        }
        default['Settings'] = {
            "commandprefix": "<",
            "placeholder": "<"
        }

        return default

    def get_config_values(self):
        data = ""
        read_list = []

        with open(self.config_path_complete) as file:
            read_list = file.readlines()

        for string in read_list:
            data += string

        return json.loads(data)
