from config import database_file
from config import DATA_FOLDER
import sqlite3, os, json


def save_to_database(job_offers_list):
    os.makedirs(DATA_FOLDER, exist_ok=True)
    conn = sqlite3.connect(database_file, isolation_level=None)
    conn.execute('CREATE TABLE IF NOT EXISTS job_offers (id INTEGER PRIMARY KEY AUTOINCREMENT,timestamp TEXT,offer_title TEXT, company_name TEXT, headquarters TEXT, post_time TEXT, categories TEXT, offer_url TEXT )')
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
        print(conn.execute('SELECT * FROM job_offers').fetchall())
    conn.close()

