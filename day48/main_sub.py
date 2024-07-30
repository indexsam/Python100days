#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By

# IMPORTANT LINK
# https://www.selenium.dev/documentation/webdriver/elements/locators/

URL = "https://www.amazon.com"
URL2= "https://www.python.org/"

# keep browser open after loading page

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(URL2)
#----------------------------------------------
# single case test
#----------------------------------------------
'''
date=driver.find_element(By.CSS_SELECTOR, ".event-widget time")
print(date.text)

event = driver.find_element(By.CSS_SELECTOR, ".event-widget li a")
print(event.text)
'''

#-------------------------
# multiple case test
#--------------------------


date=driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
dates = [d.text for d in date]


event = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = [e.text for e in event]

print(dates)
print("-----------------")
print()
print(events)

dict_events ={}
index=0
for dt, ev  in zip(dates,events):
    dict_events[index]={"time":dt, "name":ev}
    index +=1
print(dict_events)


driver.quit()
