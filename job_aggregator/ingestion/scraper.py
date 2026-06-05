import sys

from job_aggregator.core.logger import log
from playwright.sync_api import sync_playwright


def scrape_data(URL):
    log.debug("Starting playwright")
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                headless=False
            )  # 'headless = True' triggered Cloudflare anti-bot verification
            try:
                log.debug("Loading page content")
                page = browser.new_page()
                page.goto(URL, wait_until="domcontentloaded")
                page.wait_for_selector("section.jobs ul li.new-listing-container")

                raw_html = page.content()
                return raw_html
            finally:
                browser.close()
    except Exception:
        log.exception("An error occured while scraping data")
        sys.exit(1)
