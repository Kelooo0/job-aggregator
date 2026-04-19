from playwright.sync_api import sync_playwright
from core.logger import log_info
from core.logger import log_error
import sys

def scrape_data(URL):
    log_info('Starting playwright')
    with sync_playwright() as playwright:
        try:
            browser = playwright.chromium.launch(headless=False) # headless = True triggered Cloudflare anti-bot verification
        except Exception as exc:
            log_error(f'Playwright error occured, code: {exc}')
            print(f'Playwright error occured')
            sys.exit(1)
        try:
            page = browser.new_page()
            page.goto(URL, wait_until="domcontentloaded")
            page.wait_for_selector('section.jobs ul li.new-listing-container')
        except Exception as exc:
            log_error('An error occured while loading page content')
            print('An error occured while loading page content')
            sys.exit(1)
        log_info('Scraping job offers data')
        try:
            jobs = page.locator('section.jobs ul li.new-listing-container')
            count = jobs.count()
            jobs_html = []
            for i in range(count):
                jobs_html.append(jobs.nth(i).inner_html())
        except Exception as exc:
            log_error(f'An error occured while scraping data, code: {exc}')
            print(f'An error occured while scraping data')
            sys.exit(1)
        browser.close()
        return jobs_html
