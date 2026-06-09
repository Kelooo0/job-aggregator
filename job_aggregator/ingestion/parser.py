import json
import re
import sys
from datetime import UTC, datetime, timedelta

from bs4 import BeautifulSoup
from loguru import logger

from job_aggregator.core.config import config


def parse_data(raw_html):
    job_offers = []

    bs = BeautifulSoup(raw_html, "html.parser")
    jobs_html = bs.select("section.jobs ul li.new-listing-container")
    if not jobs_html:
        logger.info("No job offers found")
        sys.exit(0)
    logger.debug("Parsing job offers")
    for card in jobs_html:
        try:
            link = card.select_one("a.listing-link--unlocked")
            if not link or not link.get("href"):
                continue
            offer_url = f"{config.BASE_URL}{link['href']}"
            timestamp = datetime.now(UTC).isoformat()
            title = card.select_one("h3.new-listing__header__title")
            title = title.text.strip() if title else None

            company = card.select_one("p.new-listing__company-name")
            company = company.text.strip() if company else None

            headquarters = card.select_one("p.new-listing__company-headquarters")
            headquarters = headquarters.text.strip() if headquarters else None

            post_ago = card.select_one("p.new-listing__header__icons__date")
            post_ago = post_ago.text.strip() if post_ago else None
            post_date = None
            if post_ago:
                if re.match(r"^\d+d$", post_ago):
                    post_ago_num = int(post_ago[:-1])
                    post_ago_delta = timedelta(days=post_ago_num)
                    cur_date = datetime.now(UTC).date()
                    post_date = cur_date - post_ago_delta
                    post_date = post_date.strftime("%Y-%m-%d")

            categories = bs.select("p.new-listing__categories__category")
            job_categories = [c.text.strip() for c in categories]

            job_data = {
                "timestamp": timestamp,
                "title": title,
                "company_name": company,
                "headquarters": headquarters,
                "post_date": post_date,
                "categories": json.dumps(job_categories),
                "offer_url": offer_url,
            }
            job_offers.append(job_data)
        except Exception:
            logger.error("An error occured while parsing a job offer")
            logger.opt(exception=True).debug("Exception traceback:")
            continue
    return job_offers
