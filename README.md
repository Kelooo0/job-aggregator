# JOB TRACKER

Job Tracker uses weworkremotely.com website to scrape job offers using keyword provided by the user.
Script scrapes data, parses it, creates last report as CSV file, appends data to database and leaves a logfile.
!! Use script responsibly and introduce delays between requests to not cause disruptions

# HOW IT WORKS

1. User enters keyword
2. Script konfigures the URL
3. Playwright opens the website and scrapes job offers data
4. Parses data into workable form
5. Using formatted data creates csv report at `reports\last_report.csv`
6. Appends data to the database at `data\database.db`
7. Leaves a logfile at `logs\last_log.log`

# Structure
- `main.py` - Controls program
- `scraper.py` - Scrapes data
- `parser.py` - Parses
- `report.py` - Creates CSV report
- `database.py` - Appends data to database
- `reports\` - Holds `last_report.csv` file
- `data\` - Holds `database.db` file
- `logs\` - Holds `last_log.log` file

# Installation

1. Download project files
2. Create and activate virtual environment at projects folder
3. Install dependencies from `requirements.txt`

# HOW TO RUN

Run main.py using python
