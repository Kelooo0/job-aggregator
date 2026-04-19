import os, datetime
from core.config import Config

def log_info(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(Config.LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f'[{timestamp}] [INFO] {message}\n')

def log_error(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(Config.LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f'[{timestamp}] [ERROR] {message}\n')

def create_logfile():
    os.makedirs(Config.LOG_FOLDER, exist_ok=True)
    f = open(Config.LOG_FILE, 'w', encoding='utf-8')
    f.close()

