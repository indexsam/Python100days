#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

CLICK_MINS = 1
UPGRADES = 10

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


def call_grandma():
    grandma = driver.find_element(By.ID, "buyGrandma")
    grandma_color = grandma.get_attribute("class")
    # grandma_score = int(grandma.text.split()[2])
    return grandma, grandma_color


def call_cursor():
    cursor = driver.find_element(By.ID, "buyCursor")
    cursor_color = cursor.get_attribute("class")
    return cursor, cursor_color

def call_factory():
    factory = driver.find_element(By.ID, "buyFactory")
    factory_color = factory.get_attribute("class")
    return factory, factory_color

def call_mine():
    mine = driver.find_element(By.ID, "buyMine")
    mine_color = mine.get_attribute("class")
    return mine, mine_color

def call_shipment():
    shipment = driver.find_element(By.ID, "buyShipment")
    shipment_color = shipment.get_attribute("class")
    return shipment, shipment_color

def call_alchemy():
    alchemy = driver.find_element(By.ID, "buyAlchemy lab")
    alchemy_color = alchemy.get_attribute("class")
    return alchemy, alchemy_color

def call_portal():
    portal = driver.find_element(By.ID, "buyPortal")
    portal_color = portal.get_attribute("class")
    return portal, portal_color


def call_timemachine():
    timemachine = driver.find_element(By.ID, "buyTime machine")
    timemachine_color = timemachine.get_attribute("class")
    return timemachine, timemachine_color



counter =0
status =True
while status:
    
    start_time =time.time()
    while time.time() - start_time < (CLICK_MINS * 60):
        cookie.click()
    
    options=[]
    cur, c_col = call_cursor()
    if c_col !="grayed":
        options.append(cur)

    gran, g_col =call_grandma()
    if g_col !="grayed":
        options.append(gran)

    fac , f_col = call_factory()
    if f_col !="grayed":
        options.append(fac)

    mne, m_col = call_mine()
    if m_col !="grayed":
        options.append(mne)

    ship, s_col = call_shipment()
    if s_col !="grayed":
        options.append(ship)

    alc, a_col = call_alchemy()
    if a_col !="grayed":
        options.append(alc)

    port, p_col = call_portal()
    if p_col !="grayed":
        options.append(port)

    timm, tm_col = call_timemachine()
    if tm_col !="grayed":
        options.append(timm)


    obj = random.choice(options)
    obj.click()
    counter +=1
    if counter==UPGRADES:
        status=False


driver.quit()

