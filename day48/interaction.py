#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# IMPORTANT LINK
# https://www.selenium.dev/documentation/webdriver/elements/locators/

URL = "https://en.wikipedia.org/wiki/Main_Page"
URL2 = "http://secure-retreat-92358.herokuapp.com/"

# keep browser open after loading page

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(URL2)
##---------------------------------------
'''
# URL  for this 
count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(count.text)
'''

##----------------------------URL2 -------

in1 = driver.find_element(By.NAME, "fName")
in1.send_keys("Samuel")
in2 = driver.find_element(By.NAME, "lName")
in2.send_keys("Obadan")
in3 = driver.find_element(By.NAME, "email")
in3.send_keys("SamuelObadan@example.com")

button = driver.find_element(By.TAG_NAME, "button")
button.click()



#driver.quit()
