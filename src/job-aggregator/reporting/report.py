import csv, os, sys
from core.config import Config
from core.logger import log_info
from core.logger import log_error
from datetime import date

def get_snapshot_name():
    return f'snapshot_{date.today().isoformat()}.csv'

def check_csv():
    log_info('Checking if CSV report already exists')
    os.makedirs(Config.REPORT_FOLDER, exist_ok=True)
    filename = get_snapshot_name()
    file_path = Config.REPORT_FOLDER / filename
    if not file_path.exists():
        log_info('Creating CSV report')
        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['timestamp','title','company_name','headquarters','post_date','categories','offer_url'])
    return file_path

def save_to_csv(new_jobs):
    file_path = check_csv()
    log_info('Saving data to CSV report')
    try:
        with open(file_path, 'a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            for job in new_jobs:
                csv_writer.writerow([job.timestamp,job.title,job.company_name,job.headquarters,job.post_date,job.categories,job.offer_url])
        return file_path
    except Exception as exc:
        log_error(f'An error occured while saving data to CSV report, code: {exc}')
        print(f'An error occured while saving data to CSV report')
        sys.exit(1)
