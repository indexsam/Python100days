#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests

# IMPORTANT LINK
# https://www.selenium.dev/documentation/webdriver/elements/locators/

FORM_URL = "https://forms.gle/8Fc94GLMMRzFdqpZ6"
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

'''

#---------Boiler plate selenium---------------------
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(ZILLOW_URL)
##---------------------------------------------------
def fill_form():
    time.sleep(2)
    add = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add.send_keys("Avana drive")

    time.sleep(2)
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys("129.02")

    time.sleep(2)
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys("http://www.avana.com/news/housing")

    time.sleep(2)
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()


    time.sleep(10)
    back = driver.find_element(By.LINK_TEXT, "Submit another response")
    back.click()

#fill_form()
'''
response = requests.get(ZILLOW_URL)
response.raise_for_status()
site_data = response.text

soup = BeautifulSoup(site_data, "html.parser")
print(soup.title.getText())
'''
#---------------Testing single cases----------------------
link = soup.select_one(".StyledPropertyCardDataWrapper a")
print(link.get("href"))
print(link.getText().strip())
#----
pricing =soup.select_one(".StyledPropertyCardDataWrapper .PropertyCardWrapper__StyledPriceLine")
print(pricing.getText().split("+")[0])
#----------------------------------------------------------
'''

#---------------------Main deal-----------------

link_list = soup.select(".StyledPropertyCardDataWrapper a")
href_list= [link.get("href") for link in link_list]
address_list = [link.getText().strip() for link in link_list]
print(href_list[:2])
print("")
print("href lemnth ", len(href_list))
print(address_list[:2])
print("")
print("address lemnth ", len(address_list))

#----
pricing_list = soup.select(".StyledPropertyCardDataWrapper .PropertyCardWrapper__StyledPriceLine")
price_list = [price.getText().split("+")[0] for price in pricing_list]
print(price_list[:2])

print("price lemnth ", len(price_list))






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
'''
time.sleep(30)
inp = driver.find_element(By.TAG_NAME, "input")
inp.send_keys("samuelobad76190")
'''
# -------Possible option---------

# button = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Next')]")
# button.click()


# Using button text (out of the box)
'''
buttons = driver.find_elements(By.TAG_NAME, 'button')
next_button_custom = None
for button in buttons:
    if 'Next' in button.text:
        next_button_custom = button
        break
next_button_custom.click()


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
