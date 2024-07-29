#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()


URL = "https://appbrewery.github.io/instant_pot/"
URL_LIVE = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"


headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
           "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"}

response = requests.get(URL_LIVE, headers=headers)
data = response.text

soup = BeautifulSoup(data, "html.parser")
print(soup.title.getText())



number = soup.find(class_="a-offscreen")
# print(number)
# print(number.getText())

price_currency = number.getText()
price = price_currency.split("$")[1]
price_raw = float(price)
# print(price_raw)



url = soup.find(id="bylineInfo")
link = url.get("href")

title = soup.find(id="productTitle")
msg = title.getText().strip()
list_msg = msg.split()
string_msg =""
for i in list_msg:
    try:
        i.encode('ascii')
        string_msg+=(i.strip() +' ')
    except UnicodeEncodeError:
        print(f"skiping {i}")
        continue

# print(string_msg)




my_email="obadanindexsam@gmail.com"

def send_mail(message, price, url):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=os.getenv("PASSWORD"))
        connection.sendmail(from_addr=my_email, to_addrs="obadansam@gmail.com",
                    msg=f"Subject: Amazon Price Alert!!\n\n{message}\n ${price}\n{url}")



if price_raw < 100:
    send_mail(string_msg, price_raw, link)



