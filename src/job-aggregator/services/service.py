from ingestion.scraper import scrape_data
from core.logger import log_info, log_error
from ingestion.parser import parse_data
from storage.database import save_to_database
from reporting.report import save_to_csv
from storage.models import Job
import sys

class JobService:
    def search_jobs(self,url):
        log_info('Starting data scraping')
        jobs_html = scrape_data(url)
        log_info('Data scraped properly')
        log_info('Starting data parsing')
        job_offers = parse_data(jobs_html)
        log_info('Data parsed properly')
        try:
            jobs = [
                Job(
                    timestamp = job['timestamp'],
                    title = job['title'],
                    company_name = job['company_name'],
                    headquarters = job['headquarters'],
                    post_date = job['post_date'],
                    categories = job['categories'],
                    offer_url = job['offer_url']
                )
                for job in job_offers
            ]
        except Exception as exc:
            log_error('An error occured while building Job objects')
            print('An error occured while building Job objects')
            sys.exit(1)
        if not jobs:
            log_info('No job offers found')
            print('No job offers found')
            sys.exit(0)
        log_info('Saving new jobs to database')
        new_jobs = save_to_database(jobs)
        log_info('Data saved properly')
        log_info('Saving new jobs to CSV report')
        snapshot_path = save_to_csv(new_jobs)
        log_info('Data saved to CSV report properly')
        return jobs
