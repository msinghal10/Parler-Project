from os.path import exists 
from os import listdir
import json

settings_file_name = '.settings.json'

def config_exists():
    return exists(settings_file_name)

def generate_config():
    instance_name = input('Enter name of computer/instace: ')
    threads = int(input('Enter number of threads: '))
    delay_lb = float(input('Enter delay lower-bound: '))
    delay_ub = float(input('Enter delay upper-bound: '))
    cookies = input("Enter cookies: ")
    key = input("Enter API key: ")
    data = {'name': instance_name, 'threads': threads, 'delay_lb': delay_lb, 'delay_ub': delay_ub, 'cookies': cookies, 'key': key}
    with open(settings_file_name, 'w') as f:
        json.dump(data, f)

def read_config():
    with open(settings_file_name, 'r') as f:
        return json.load(f)

def read_input_file_candidates():
    files = []

    for file in listdir('.'):
        if file.endswith(".csv"):
            files.append(file)

    return files