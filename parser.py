from scraper import scrape_data
from bs4 import BeautifulSoup
from config import BASE_URL
import re, datetime, sys
from logger import log_info
from logger import log_error

def data_parser(jobs_list_html):
    log_info('Parsing offer data')
    job_offers_list = []
    try:
        for i, job in enumerate(jobs_list_html):
            job_offer = {}
            categories_list = []

            bs = BeautifulSoup(job, 'html.parser')
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            title = bs.select_one('h3.new-listing__header__title').get_text().strip()
            company = bs.select_one('p.new-listing__company-name').get_text().strip()
            headquarters = bs.select_one('p.new-listing__company-headquarters').get_text().strip()
            post_time = bs.select_one('p.new-listing__header__icons__date').get_text().strip()
            if re.match(r'^\d+d$', post_time):
                post_days_ago = post_time[:-1]
                post_delta = datetime.timedelta(days=int(post_days_ago))
                cur_date = datetime.datetime.now()
                post_time = cur_date - post_delta
                post_time = post_time.strftime('%Y-%m-%d')
            categories = bs.select('p.new-listing__categories__category')
            for cat in categories:
                categories_list.append(cat.get_text().strip())
            link = bs.select_one('a.listing-link--unlocked')
            link_href = link['href'] if link else None
            offer_link = f'{BASE_URL}{link_href}'

            job_offer['timestamp'] = timestamp
            job_offer['offer_title'] = title
            job_offer['company_name'] = company
            job_offer['headquarters'] = headquarters
            job_offer['post_time'] = post_time
            job_offer['categories'] = categories_list
            job_offer['offer_url'] = offer_link
            job_offers_list.append(job_offer)
    except Exception as exc:
        print(f'An error occured during parsing data')
        log_error(f'An error occured during parsing data, code : {exc}')
        sys.exit(1)
    return job_offers_list
