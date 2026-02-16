import csv, os, sys
from config import report_file
from config import REPORT_FOLDER
from logger import log_info
from logger import log_error

def save_to_csv(job_offers_list):
    log_info('Creating CSV report')
    os.makedirs(REPORT_FOLDER, exist_ok=True)
    try:
        with open(report_file, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['timestamp','offer_title','company_name','headquarters','post_time','categories','offer_url'])
            for job_offer in job_offers_list:
                timestamp = job_offer['timestamp']
                offer_title = job_offer['offer_title']
                company_name = job_offer['company_name']
                headquarters = job_offer['headquarters']
                post_time = job_offer['post_time']
                categories = job_offer['categories']
                offer_url = job_offer['offer_url']
                csv_writer.writerow([timestamp,offer_title,company_name,headquarters,post_time,categories,offer_url])
    except Exception as exc:
        print(f'An error occured during creating CSV report')
        log_error(f'An error occured during creating CSV report, code: {exc}')
        sys.exit(1)
