from pathlib import Path

class Config:
    BASE_URL = 'https://weworkremotely.com'

    BASE_DIR = Path(__file__).resolve().parents[3]

    REPORT_FOLDER = BASE_DIR / "reports"
    DATA_FOLDER = BASE_DIR / "data"
    LOG_FOLDER = BASE_DIR / "logs"

    REPORT_FILE = REPORT_FOLDER / "report.csv"
    DATABASE_FILE = DATA_FOLDER / "database.db"
    LOG_FILE = LOG_FOLDER / "app.log"

def build_url(keyword):
    url = f'https://weworkremotely.com/remote-jobs/search?search_uuid=&sort=&term={keyword}&categories_chosen=&countries_chosen=&chosen-salary_range=&skills_chosen='
    return url


