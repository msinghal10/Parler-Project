from os.path import exists 
import json

settings_file_name = '.settings.json'

def config_exists():
    return exists(settings_file_name)

def generate_config():
    instance_name = input('Enter name of computer/instace: ')
    threads = int(input('Enter number of threads: '))
    delay_lb = float(input('Enter delay lowe-bound: '))
    delay_ub = float(input('Enter delay upper-bound: '))