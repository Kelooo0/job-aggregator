import sys

from loguru import logger
from job_aggregator.ingestion.parser import parse_data
from job_aggregator.ingestion.scraper import scrape_data
from job_aggregator.reporting.report import save_to_csv
from job_aggregator.storage.database import save_to_database
from job_aggregator.storage.models import Job


def search_jobs(url):
    logger.info("Scraping data")
    raw_html = scrape_data(url)
    logger.info("Fetched page content")
    logger.info("Parsing data")
    job_offers = parse_data(raw_html)
    logger.info("Data parsed properly")
    jobs = []
    for job in job_offers:
        try:
            job_obj = Job(
                timestamp=job["timestamp"],
                title=job["title"],
                company_name=job["company_name"],
                headquarters=job["headquarters"],
                post_date=job["post_date"],
                categories=job["categories"],
                offer_url=job["offer_url"],
            )
            jobs.append(job_obj)
        except Exception:
            logger.error("An error occured while validating a job offers data")
            logger.opt(exception=True).debug("Exception traceback:")
            continue
    if not jobs:
        logger.info("No job offers found")
        sys.exit(0)
    logger.info("Saving new jobs to database")
    new_jobs = save_to_database(jobs)
    logger.info("Data saved to database correctly")
    logger.info("Saving new jobs to a CSV report")
    save_to_csv(new_jobs)
    logger.info("Data saved to CSV report properly")
    return jobs
