from playwright.sync_api import sync_playwright

def scrape_data(URL):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False) # Script could'nt scrape data properly with headless True
        page = browser.new_page()
        page.goto(URL)

        jobs = page.locator('section.jobs ul li.new-listing-container').first
        count = jobs.count()

        if count == 0:
            print('No job offers found for input keyword')
        else:
            print(f'{count} job offers found')
        jobs_list_html = []
        for i in range(count):
            jobs_list_html.append(jobs.nth(i).inner_html())
        browser.close()
        return jobs_list_html
