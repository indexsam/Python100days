#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# IMPORTANT LINK
# https://www.selenium.dev/documentation/webdriver/elements/locators/

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3984928692&distance=25&f_AL=true&f_WT=2&geoId=101174742&keywords=data%20analyst&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true"

# keep browser open after loading page

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
##---------------------------------------


'''
in1 = driver.find_element(By.NAME, "fName")
in1.send_keys("Samuel")
in2 = driver.find_element(By.NAME, "lName")
in2.send_keys("Obadan")
in3 = driver.find_element(By.NAME, "email")
in3.send_keys("SamuelObadan@example.com")

button = driver.find_element(By.TAG_NAME, "button")
button.click()
'''

time.sleep(300)

driver.quit()
