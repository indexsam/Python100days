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



#---------Boiler plate selenium---------------------

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

##---------------------------------------------------
def fill_form(address_input, price_input, href_input):
    driver.get(FORM_URL)

    time.sleep(2)
    add = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add.send_keys(f"{address_input}")

    time.sleep(2)
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(f"{price_input}")

    time.sleep(2)
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(f"{href_input}")

    time.sleep(2)
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()


    time.sleep(10)
    back = driver.find_element(By.LINK_TEXT, "Submit another response")
    back.click()



#  ZILLOW
def zillow():
    response = requests.get(ZILLOW_URL)
    response.raise_for_status()
    site_data = response.text

    soup = BeautifulSoup(site_data, "html.parser")
    print(soup.title.getText())


    link_list = soup.select(".StyledPropertyCardDataWrapper a")
    href_list= [link.get("href") for link in link_list]
    address_list = [link.getText().strip() for link in link_list]

    #  GetPrice

    pricing_list = soup.select(".StyledPropertyCardDataWrapper .PropertyCardWrapper__StyledPriceLine")
    price_list = [price.getText().split("+")[0] for price in pricing_list]

    return address_list, price_list, href_list

address, price, link = zillow()


list_of_dict=[]

for add, pr, ln in zip(address,price,link):
    list_of_dict.append({"address":add, "price":pr, "link":ln})


for data in list_of_dict:
    fill_form(data["address"], data["price"], data["link"])

time.sleep(2)
driver.quit()
