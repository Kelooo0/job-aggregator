import os

BASE_URL = 'https://weworkremotely.com'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_FOLDER = os.path.join(BASE_DIR,'reports')
DATA_FOLDER = os.path.join(BASE_DIR,'data')
LOG_FOLDER = os.path.join(BASE_DIR,'logs')
report_file = os.path.join(REPORT_FOLDER, 'last_report.csv')
database_file = os.path.join(DATA_FOLDER,'database.db')
log_file = os.path.join(LOG_FOLDER,'last_log.log')

def url_config(keyword):
    URL = f'https://weworkremotely.com/remote-jobs/search?search_uuid=&sort=&term={keyword}&categories_chosen=&countries_chosen=&chosen-salary_range=&skills_chosen='
    return URL


