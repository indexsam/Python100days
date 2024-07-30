#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
MINS =1

# IMPORTANT LINK
# https://www.selenium.dev/documentation/webdriver/elements/locators/

URL = "https://orteil.dashnet.org/experiments/cookie/"


# keep browser open after loading page

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
#----------------------------------------------

# obj.get_name
# obj.get_attribute("id") class , name

#----------------------------------
cookie=driver.find_element(By.ID, "cookie")

grandma = driver.find_element(By.ID, "buyGrandma")
grandma_color = grandma.get_attribute("class")
grandma_score = int(grandma.text.split()[2])

print("grandma color ", grandma_color)
print("grandma score  ", grandma_score)

def call_cursor():
    cursor = driver.find_element(By.ID, "buyCursor")
    cursor_color = cursor.get_attribute("class")
    cursor_score = int(cursor.text.split()[2])

    print("cursor color ", cursor_color)
    print("cursor score  ", cursor_score)

    return cursor

counter =0
status =True
while status:
    
    start_time =time.time()
    while time.time() - start_time < (MINS * 60):
        cookie.click()
    
    cursor= call_cursor()
    cursor.click()
    counter +=1
    if counter==5:
        status=False


driver.quit()

