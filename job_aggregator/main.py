import sys

from loguru import logger

from job_aggregator.core.config import config
from job_aggregator.services.service import search_jobs


def main():
    logger.remove()
    logger.add(
        sys.stderr, level="INFO", format="<level>{level: <8}</level> | {message}"
    )
    logger.add(config.LOG_FILE, level="DEBUG", mode="w")

    logger.debug("App start")
    print("Enter job title / company name / keyword:")
    keyword = input(">")
    url = config.build_url(keyword)
    logger.debug(f"Built URL: {url}")
    logger.info(f"Searching for jobs matching '{keyword}'")
    jobs = search_jobs(url)
    logger.info("Printing found jobs")
    for idx, job in enumerate(jobs):
        print(f"""

        {idx + 1})
        Offer title: {job.title}
        Company name: {job.company_name}
        Headquarters: {job.headquarters}
        Post date: {job.post_date}
        Categories: {job.categories}
        URL: {job.offer_url}

        """)
    job_count = len(jobs)
    print(f"{job_count} job offers found")
    logger.debug("App end")


if __name__ == "__main__":
    main()
