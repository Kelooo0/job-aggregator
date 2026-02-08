from scraper import scrape_data
from parser import data_parser
from config import url_config

def main():
    print('Welcome to Job Tracker')
    print('The tracker uses weworkremotely.com to scrape job offers')
    print('Use this scraper responsibly. Introduce delays between requests to minimize server load and avoid causing disruptions.')
    print('Enter Jobtitle/company/keyword')
    keyword = input('>')
    URL = url_config(keyword)
    jobs_list_html = scrape_data(URL)
    print(jobs_list_html)
    job_offers_list = data_parser(jobs_list_html)

if __name__ == '__main__':
    main()
