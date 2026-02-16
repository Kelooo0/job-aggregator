from config import database_file
from config import DATA_FOLDER
import sqlite3, os, json, sys
from logger import log_info
from logger import log_error

def save_to_database(job_offers_list):
    log_info('Appending data to database')
    os.makedirs(DATA_FOLDER, exist_ok=True)
    try:
        conn = sqlite3.connect(database_file, isolation_level=None)
        conn.execute('CREATE TABLE IF NOT EXISTS job_offers (id INTEGER PRIMARY KEY AUTOINCREMENT,timestamp TEXT,offer_title TEXT, company_name TEXT, headquarters TEXT, post_time TEXT, categories TEXT, offer_url TEXT )')
    except Exception as exc:
        print(f'An error occured during connecting to database and creating table')
        log_error(f'An error occured during connecting to database and creating table, code: {exc}')
    try:
        for job_offer in job_offers_list:
            timestamp = job_offer['timestamp']
            offer_title = job_offer['offer_title']
            company_name = job_offer['company_name']
            headquarters = job_offer['headquarters']
            post_time = job_offer['post_time']
            categories_list = job_offer['categories']
            categories_str = json.dumps(categories_list)
            offer_url = job_offer['offer_url']
            conn.execute('INSERT INTO job_offers (timestamp,offer_title,company_name,headquarters,post_time,categories,offer_url) VALUES (?,?,?,?,?,?,?)',(timestamp,offer_title,company_name,headquarters,post_time,categories_str,offer_url))
    except Exception as exc:
        print(f'Could\'t properly append data to database')
        log_error(f'Could\'t properly append data to database, code: {exc}')
        sys.exit(1)
    conn.close()

