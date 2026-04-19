from bs4 import BeautifulSoup
from core.config import Config
from core.logger import log_info
from core.logger import log_error
import re, datetime, sys, json

def parse_data(jobs_html):
    log_info('Parsing job offers data')
    job_offers = []
    try:
        for job in jobs_html:
            job_data = {}
            job_categories = []

            bs = BeautifulSoup(job, 'html.parser')
            link = bs.select_one('a.listing-link--unlocked')
            if not link or not link.get('href'):
                continue
            offer_url = f'{Config.BASE_URL}{link['href']}'
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            title = bs.select_one('h3.new-listing__header__title')
            if title:
                title = title.get_text().strip()
            else:
                title = None
            company = bs.select_one('p.new-listing__company-name')
            if company:
                company = company.get_text().strip()
            else:
                company = None
            headquarters = bs.select_one('p.new-listing__company-headquarters')
            if headquarters:
                headquarters = headquarters.get_text().strip()
            else:
                headquarters = None
            post_time = bs.select_one('p.new-listing__header__icons__date')
            post_date = None
            if post_time:
                post_time = post_time.get_text().strip()
                if re.match(r'^\d+d$', post_time):
                    post_days_ago = post_time[:-1]
                    post_delta = datetime.timedelta(days=int(post_days_ago))
                    cur_date = datetime.datetime.now()
                    post_time = cur_date - post_delta
                    post_date = post_time.strftime('%Y-%m-%d')
            categories = bs.select('p.new-listing__categories__category')
            for cat in categories:
                job_categories.append(cat.get_text().strip())

            job_data['timestamp'] = timestamp
            job_data['title'] = title
            job_data['company_name'] = company
            job_data['headquarters'] = headquarters
            job_data['post_date'] = post_date
            job_data['categories'] = json.dumps(job_categories)
            job_data['offer_url'] = offer_url
            job_offers.append(job_data)
    except Exception as exc:
        log_error(f'An error occured while parsing data, code : {exc}')
        print('An error occured while parsing data')
        sys.exit(1)
    return job_offers
