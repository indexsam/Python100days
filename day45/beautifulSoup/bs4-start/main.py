#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
data = response.text
soup = BeautifulSoup(data, "html.parser")

print(soup.title)

val = soup.select_one(".titleline a")
print(val.getText())
print(val.get("href"))
print(soup.select_one(".score").getText())
