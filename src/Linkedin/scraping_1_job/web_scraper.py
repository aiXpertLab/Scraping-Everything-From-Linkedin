# web_scraper.py
from selenium import webdriver
from selenium.webdriver.common.by import By

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
