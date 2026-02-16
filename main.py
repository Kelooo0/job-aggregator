from scraper import scrape_data
from parser import data_parser
from config import url_config
from report import save_to_csv
from database import save_to_database
from logger import log_info
from logger import log_error
from logger import create_logfile

def main():
    create_logfile()
    log_info('Program start')
    print('Welcome to Job Tracker')
    print('The tracker uses weworkremotely.com to scrape job offers')
    print('Use this scraper responsibly. Introduce delays between requests to minimize server load and avoid causing disruptions.')
    print('Enter Jobtitle/company/keyword')
    keyword = input('>')
    log_info('Keyword obtained')
    URL = url_config(keyword)
    log_info('URL configured')
    jobs_list_html = scrape_data(URL)
    log_info('Obtained list of html job offers data')
    job_offers_list = data_parser(jobs_list_html)
    log_info('Obtained parsed list of job offers data')
    save_to_csv(job_offers_list)
    log_info('CSV report created succesfully')
    save_to_database(job_offers_list)
    log_info('Succesfully appended to database')
    log_info('Program end')
if __name__ == '__main__':
    main()
