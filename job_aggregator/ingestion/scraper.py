import sys

from playwright.sync_api import sync_playwright

from loguru import logger


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
                page.wait_for_selector("section.jobs ul li.new-listing-container")

                raw_html = page.content()
                return raw_html
            finally:
                browser.close()
    except Exception:
        logger.error("An error occured while scraping data")
        logger.opt(exception=True).debug("Scraper exception traceback:")
        sys.exit(1)
