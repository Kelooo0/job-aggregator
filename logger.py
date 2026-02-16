import os, datetime
from config import LOG_FOLDER
from config import log_file


def log_info(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f'[{timestamp}] [INFO] {message}\n')

def log_error(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f'[{timestamp}] [ERROR] {message}\n')

def create_logfile():
    os.makedirs(LOG_FOLDER, exist_ok=True)
    f = open(log_file, 'w', encoding='utf-8')
    f.close()

