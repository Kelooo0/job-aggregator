from playwright.sync_api import sync_playwright
from logger import log_info
from logger import log_error
import sys

def scrape_data(URL):
    log_info('Starting playwright')
    with sync_playwright() as playwright:
        try:
            browser = playwright.chromium.launch(headless=False) # Script could'nt scrape data properly with headless True
        except Exception as exc:
            print(f'Playwright error occured')
            log_error(f'Playwright error occured, code: {exc}')
            sys.exit(1)
        page = browser.new_page()
        page.goto(URL)
        log_info('Website opened using provided URL')
        log_info('Scraping job offers data')
        try:
            jobs = page.locator('section.jobs ul li.new-listing-container').first
            count = jobs.count()

            if count == 0:
                print('No job offers found for input keyword')
            elif count == 1:
                print('1 job offer found')
            else:
                print(f'{count} job offers found')

            jobs_list_html = []
            for i in range(count):
                jobs_list_html.append(jobs.nth(i).inner_html())
        except Exception as exc:
            print(f'Data couldn\'t be scraped properly')
            log_error(f'Data couldn\'t be scraped properly, code: {exc}')
            sys.exit(1)
        browser.close()
        return jobs_list_html
