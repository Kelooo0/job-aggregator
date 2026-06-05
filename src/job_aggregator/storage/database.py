import os
import sqlite3
import sys

from core.config import Config
from core.logger import log


def save_to_database(jobs):
    os.makedirs(Config.DATA_FOLDER, exist_ok=True)
    log.debug("Connecting to database and creating tables")
    try:
        conn = sqlite3.connect(Config.DATABASE_FILE, isolation_level=None)
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS job_offers (id INTEGER PRIMARY KEY,timestamp TEXT,title TEXT, company_name TEXT, headquarters TEXT, post_date TEXT, categories TEXT, offer_url TEXT UNIQUE )"
        )
    except Exception:
        log.exception(
            "An error occured while connecting to database and creating tables"
        )
        sys.exit(1)
    log.debug("Appending data to database")
    try:
        offer_urls = cursor.execute("SELECT offer_url FROM job_offers").fetchall()
        existing_urls = {row[0] for row in offer_urls}
        new_jobs = [
            j for j in jobs if j.offer_url and j.offer_url not in existing_urls
        ]
        # new_jobs will be used for saving to CSV report later
        # DB handles duplicates by UNIQUE + OR IGNORE
        for job in jobs:
            cursor.execute(
                "INSERT OR IGNORE INTO job_offers (timestamp,title,company_name,headquarters,post_date,categories,offer_url) VALUES (?,?,?,?,?,?,?)",
                (
                    job.timestamp,
                    job.title,
                    job.company_name,
                    job.headquarters,
                    job.post_date,
                    job.categories,
                    job.offer_url,
                ),
            )
        conn.commit()
        conn.close()
        return new_jobs
    except Exception:
        log.exception("An error occured while appending data to database")
        sys.exit(1)
