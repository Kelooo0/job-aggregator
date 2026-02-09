from scraper import scrape_data
from parser import data_parser
from config import url_config
from report import save_to_csv
from database import save_to_database

def main():
    print('Welcome to Job Tracker')
    print('The tracker uses weworkremotely.com to scrape job offers')
    print('Use this scraper responsibly. Introduce delays between requests to minimize server load and avoid causing disruptions.')
    print('Enter Jobtitle/company/keyword')
    keyword = input('>')
    URL = url_config(keyword)
    jobs_list_html = scrape_data(URL)
    job_offers_list = data_parser(jobs_list_html)
    save_to_csv(job_offers_list)
    save_to_database(job_offers_list)
if __name__ == '__main__':
    main()
