import csv
import os
import sys
from datetime import date

from core.config import config
from core.logger import log


def get_snapshot_name():
    log.debug("Setting up snapshotname")
    return f"snapshot_{date.today().isoformat()}.csv"


def check_csv():
    log.debug("Checking if CSV report already exists")
    os.makedirs(config.REPORT_FOLDER, exist_ok=True)
    filename = get_snapshot_name()
    file_path = config.REPORT_FOLDER / filename
    if not file_path.exists():
        log.debug("Creating CSV report file")
        with open(file_path, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(
                [
                    "timestamp",
                    "title",
                    "company_name",
                    "headquarters",
                    "post_date",
                    "categories",
                    "offer_url",
                ]
            )
    return file_path


def save_to_csv(new_jobs):
    file_path = check_csv()
    log.debug("Saving data to a CSV report")
    try:
        with open(file_path, "a", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            for job in new_jobs:
                csv_writer.writerow(
                    [
                        job.timestamp,
                        job.title,
                        job.company_name,
                        job.headquarters,
                        job.post_date,
                        job.categories,
                        job.offer_url,
                    ]
                )
        return file_path
    except Exception:
        log.exception("An error occured while saving data to CSV report")
        sys.exit(1)
