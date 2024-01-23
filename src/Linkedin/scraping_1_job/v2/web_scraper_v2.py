# web_scraper.py
import os
import tkinter as tk

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
user_name = os.getenv('LD_USR')
password = os.getenv('LD_KEY')

class WebScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(11)

    def login(self, username, password):
        self.driver.get('https://www.linkedin.com/login')
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def navigate_to_jobs(self):
        # self.driver.find_element(By.XPATH, "//*[@id='global-nav']/div/nav/ul/li[3]/a").click()
        self.driver.get('https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3804435648&discover=recommended')

    def scrape_job_title_and_company_name(self):
        try:
            job_title = self.driver.find_element(By.CLASS_NAME, 'job-details-jobs-unified-top-card__job-title-link')
            company_name = self.driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/div')
            
            return job_title.text, company_name.text
        except Exception as e:
            print(f"Error while scraping job title and company name: {e}")
            return None, None

    def scrape_job_desc(self):
        try:
            job_desc = self.driver.find_element(By.XPATH, '//*[@id="job-details"]')
            return job_desc.text
        except Exception as e:
            print(f"Error while scraping job description: {e}")
            return None

    def close_browser(self):
        self.driver.quit()

class TkWin:
    def __init__(self, master):
        self.master = master
        self.master.title("Web Scraper GUI")

        self.web_scraper = WebScraper()

        tk.Label(master, text="Click the button to perform the action:").pack()

        tk.Button(master, text="Login",             command=self.perform_login).pack()
        tk.Button(master, text="Navigate to Jobs",  command=self.navigate_to_jobs).pack()
        tk.Button(master, text="Title",             command=self.scrape_title).pack()
        tk.Button(master, text="Company Name",      command=self.scrape_company_name).pack()
        tk.Button(master, text="Job Desc",          command=self.scrape_job_desc).pack()

    def perform_login(self):
        self.web_scraper.login(user_name, password)

    def navigate_to_jobs(self):
        self.web_scraper.navigate_to_jobs()

    def scrape_title(self):
        job_title, _ = self.web_scraper.scrape_job_title_and_company_name()
        self.display_result("Job Title", job_title)

    def scrape_company_name(self):
        _, company_name = self.web_scraper.scrape_job_title_and_company_name()
        self.display_result("Company Name", company_name)

    def scrape_job_desc(self):
        job_desc = self.web_scraper.scrape_job_desc()
        self.display_result("Job Description", job_desc)

    def display_result(self, label, result):
        result_window = tk.Toplevel(self.master)
        result_window.title(label)
        tk.Label(result_window, text=result).pack()

    def run(self):
        self.master.mainloop()

