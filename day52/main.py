#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# IMPORTANT LINK
# https://www.selenium.dev/documentation/webdriver/elements/locators/

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3984928692&distance=25&f_AL=true&f_WT=2&geoId=101174742&keywords=data%20analyst&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true"

URL2 = "https://tinder.com/app/recs"

URL3 = "https://x.com/i/flow/login"

URL4 ="https://www.speedtest.net/"
# keep browser open after loading page

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(URL3)
##---------------------------------------
'''
def get_SpeedData():
    download = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
    upload = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    return download, upload

obj1 = driver.find_element(By.CSS_SELECTOR, ".start-button a")
obj1.click()


time.sleep(60)
down, up = get_SpeedData()

print(f"Download speed: {down} and Upload speed: {up}")

time.sleep(10)
driver.quit()
'''
#----------------------------------------------------------

time.sleep(30)
inp = driver.find_element(By.TAG_NAME, "input")
inp.send_keys("samuelobad76190")

# -------Possible option---------

# button = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Next')]")
# button.click()


# Using button text (out of the box)

buttons = driver.find_elements(By.TAG_NAME, 'button')
next_button_custom = None
for button in buttons:
    if 'Next' in button.text:
        next_button_custom = button
        break
next_button_custom.click()

'''
next = driver.find_elements(By.TAG_NAME, "button")
print("number of buttons username: ", len(next))
next[3].click() # next button

# NEXT page

time.sleep(2)
inp_pass = driver.find_element(By.NAME, "password")
inp_pass.send_keys("123")


password = driver.find_elements(By.TAG_NAME, "button")
print("number of buttons password: ", len(password))
password[4].click() # login button

'''

#--------------------Archive-------------------
'''
in1 = driver.find_element(By.NAME, "fName")
in1.send_keys("Samuel")
in2 = driver.find_element(By.NAME, "lName")
in2.send_keys("Obadan")
in3 = driver.find_element(By.NAME, "email")
in3.send_keys("SamuelObadan@example.com")

button = driver.find_element(By.TAG_NAME, "button")
button.click()


time.sleep(10)

driver.quit()
'''
#--------------------------------------------
