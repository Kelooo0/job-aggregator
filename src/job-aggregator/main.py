from core.logger import create_logfile
from core.logger import log_info
from core.config import build_url
from services.service import JobService
def main():
    create_logfile()
    log_info('Job aggregator started')
    log_info('Created log file')
    print("Enter job title / company name / keyword:")
    keyword = input('>')
    URL = build_url(keyword)
    log_info('URL built')
    service = JobService()
    jobs = service.search_jobs(URL)
    log_info('Printing jobs data')
    for idx, job in enumerate(jobs):
        print(f'''

        {idx+1})
        Offer title: {job.title}
        Company name: {job.company_name}
        Headquarters: {job.headquarters}
        Post date: {job.post_date}
        Categories: {job.categories}
        URL: {job.offer_url}

        ''')
    log_info('Job aggregator ended')

if __name__ == '__main__':
    main()
