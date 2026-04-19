# JOB TRACKER

Job Tracker uses weworkremotely.com website to scrape job offers using keyword provided by the user.
Script scrapes data, parses it, appends data to database, appends data to todays snapshot as CSV file and leaves a logfile.
!! Use script responsibly and introduce delays between requests to not cause disruptions

# HOW IT WORKS

1. User enters keyword
2. Script konfigures the URL
3. Playwright opens the website and scrapes job offers data
4. Parses data into workable form
5. Using formatted data creates csv report at `reports\snapshot{today's_date}.csv`
6. Appends data to the database at `data\database.db`
7. Leaves a logfile at `logs\app.log`

# Structure
- `main.py` - Controls program
- `scraper.py` - Scrapes data
- `parser.py` - Parses data
- `database.py` - Appends data to database
- `report.py` - Creates CSV report
- `data\` - Holds `database.db` file
- `logs\` - Holds `app.log` file
- `reports\` - Holds snapshot CSV file

# Installation

1. Clone repository files
    - git clone https://github.com/Kelooo0/job-aggregator.git

2. Create and activate virtual environment at projects folder
    - Windows: python -m venv .venv
    - Linux/macOS : python3 -m venv .venv
    <br>
    - Windows: .venv\Scripts\activate
    - Linux/macOS: source venv/bin/activate

3. Install dependencies from `requirements.txt`

# HOW TO RUN

- cd src/job-aggregator
- Run main.py using dedicated terminal
