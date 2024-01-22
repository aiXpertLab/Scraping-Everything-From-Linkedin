# main.py
import os
from dotenv import load_dotenv
from Linkedin.scraping_1_job.web_scraper1 import WebScraper

load_dotenv()
user_name = os.getenv('LD_USR')
password = os.getenv('LD_KEY')

if __name__ == "__main__":
    web_scraper = WebScraper()

    try:
        web_scraper.login(user_name, password)
        web_scraper.navigate_to_jobs()

        job_title, company_name, job_desc = web_scraper.scrape_job_details()

        print("Job Title:", job_title)
        print("Company Name:", company_name)
        print("Job Description:", job_desc)

    finally:
        web_scraper.close_browser()
