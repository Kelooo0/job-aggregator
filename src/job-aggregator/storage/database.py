from core.config import Config
import sqlite3, os, sys
from core.logger import log_info
from core.logger import log_error

def save_to_database(jobs):
    os.makedirs(Config.DATA_FOLDER, exist_ok=True)
    log_info('Creating connection with the database')
    try:
        conn = sqlite3.connect(Config.DATABASE_FILE, isolation_level=None)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS job_offers (id INTEGER PRIMARY KEY,timestamp TEXT,title TEXT, company_name TEXT, headquarters TEXT, post_date TEXT, categories TEXT, offer_url TEXT UNIQUE )')
    except Exception as exc:
        log_error(f'An error occured while connecting to database and creating table, code: {exc}')
        print(f'An error occured while connecting to database and creating table')
        sys.exit(1)
    log_info('Appending data to database')
    try:
        offer_urls = cursor.execute('SELECT offer_url FROM job_offers').fetchall()
        existing_urls = {row[0] for row in offer_urls}
        new_jobs = [
            job for job in jobs
            if job.offer_url and job.offer_url not in existing_urls
        ]
        # new_jobs will be used for saving to CSV report later
        # DB handles duplicates by UNIQUE + OR IGNORE
        for job in jobs:
            cursor.execute('INSERT OR IGNORE INTO job_offers (timestamp,title,company_name,headquarters,post_date,categories,offer_url) VALUES (?,?,?,?,?,?,?)',(
            job.timestamp,
            job.title,
            job.company_name,
            job.headquarters,
            job.post_date,
            job.categories,
            job.offer_url
            ))
        return new_jobs
    except Exception as exc:
        log_error(f'An error occured while appending data to database, code: {exc}')
        print(f'An error occured while appending data to database')
        sys.exit(1)
    conn.commit()
    conn.close()
