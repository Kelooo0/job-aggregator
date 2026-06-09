import sys

from loguru import logger
from playwright.sync_api import sync_playwright


def scrape_data(URL):
    logger.debug("Starting playwright")
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                headless=False
            )  # 'headless = True' triggered Cloudflare anti-bot verification
            try:
                logger.debug("Loading page content")
                page = browser.new_page()
                page.goto(URL, wait_until="domcontentloaded")

                raw_html = page.content()
                return raw_html
            finally:
                browser.close()
    except Exception:
        logger.error("An error occured while scraping data")
        logger.opt(exception=True).debug("Scraper exception traceback:")
        sys.exit(1)
