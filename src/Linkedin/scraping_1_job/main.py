# main.py
import os
from dotenv import load_dotenv
import tkinter as tk
from web_scraper import WebScraper

load_dotenv()
user_name = os.getenv('LD_USR')
password = os.getenv('LD_KEY')

class WebScraperApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Web Scraper GUI")

        self.web_scraper = WebScraper()

        tk.Label(master, text="Click the button to perform the action:").pack()

        tk.Button(master, text="Login", command=self.perform_login).pack()
        tk.Button(master, text="Navigate to Jobs", command=self.navigate_to_jobs).pack()
        tk.Button(master, text="Title", command=self.scrape_title).pack()
        tk.Button(master, text="Company Name", command=self.scrape_company_name).pack()
        tk.Button(master, text="Job Desc", command=self.scrape_job_desc).pack()

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

if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperApp(root)
    app.run()
