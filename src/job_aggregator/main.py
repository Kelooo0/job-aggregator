from core.config import config
from core.logger import log
from services.service import search_jobs


def main():
    log.debug("App start")
    print("Enter job title / company name / keyword:")
    keyword = input(">")
    url = config.build_url(keyword)
    log.debug(f"Built URL: {url}")
    log.info(f"Searching for jobs matching '{keyword}'")
    jobs = search_jobs(url)
    log.info("Printing found jobs")
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
    log.debug("App end")


if __name__ == "__main__":
    main()
