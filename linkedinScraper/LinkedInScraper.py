from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from parsel import Selector
import variables
import os
import time
import parsel
import csv

# Step 1: Login to LinkedIn

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
driver.get("https://linkedin.com/login")
time.sleep(2)

# Input username and password from variables file
username = driver.find_element(By.ID, "username")
username.send_keys(variables.linkedin_username)
time.sleep(2)
password = driver.find_element(By.ID, "password")
password.send_keys(variables.linkedin_password)
time.sleep(2)

# Click Login Button
log_in_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button') 
log_in_button.click()
time.sleep(3)


##Link url file path to current directory
dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "SubURLs.txt")

## Open file of URLs
ccfile = open(lines)

scribe = csv.writer(open(variables.file_name, 'w'))
scribe.writerow(['Name', 'Job title', 'Company', 'Connections'])

## Parse file one line at a time
for line in ccfile:
    values = line.split()
    driver.get(values[0])
    time.sleep(2)
    driver.page_source
    sel = Selector(text=driver.page_source)

    name = sel.xpath('//h1/text()').extract_first()
    if name:
        name = name.strip()
    print(name)

    # xpath to extract the text from the class containing the job title
    job_title = sel.xpath('//*[contains(@class, "ph5")]/div[2]/div[1]/div[2]/text()').extract_first()

#   job_title = sel.xpath('//*[starts-with(@class, "ph5 pb5")]/div[2]/div[1]/div[2]/text()').extract_first()

    if job_title:
        job_title = job_title.strip()
    print(job_title)


## xpath to extract the text from the class containing the company
    company = sel.xpath('//*[contains(@class, "pv-top-card")]/div[2]/div[2]//ul/li[1]/button/span/div/text()').extract_first()

    if company:
        company = company.strip()
    print(company)

## extract number of connections

    connections = sel.xpath('//*[contains(@class, "pv-top-card")]/div[2]/ul/li/span/span').extract_first()

    if connections:
        connections = connections.strip('<span class="t-bold">')
        connections = connections.strip("</span>")
    print(connections)


# /html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/ul/li[2]/span/span
# /html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/ul/li/span/text()

    time.sleep(2)

    scribe.writerow([name, job_title, company, connections])

    time.sleep(10)
ccfile.close()