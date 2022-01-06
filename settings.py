from os.path import exists 

settings_file_name = '.settings.json'

def config_exists():
    return exists(settings_file_name)