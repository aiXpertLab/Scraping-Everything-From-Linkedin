# job_scraper.py
from selenium.webdriver.common.by import By

class JobScraper:
    @staticmethod
    def scrape_job_details(driver):
        job_desc = driver.find_element(By.XPATH, '//*[@id="job-details"]')
        return job_desc.text
