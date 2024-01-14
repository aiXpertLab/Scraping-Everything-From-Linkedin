'''
My Module: including:
1. Linkedin_scraping_all_jobs_details 
'''

# Linkedin_scraping_all_jobs_details
job_titles = []
company_names = []
company_locations = []
work_methods = []
post_dates = []
work_times = []
job_desc = []

i, j = 0, 0

def add_job_data(title, company, location, method, date, time, desc):
    """
    Function to add job data to the lists
    """
    job_titles.append(title)
    company_names.append(company)
    company_locations.append(location)
    work_methods.append(method)
    post_dates.append(date)
    work_times.append(time)
    job_desc.append(desc)