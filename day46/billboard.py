#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup


date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ").strip()

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
data = response.text


soup = BeautifulSoup(data, "html.parser")
print(soup.title.getText())


music = soup.select("li ul li h3")
music100 = [title.getText().strip() for title in music]
print(music100[:10])






'''

music = soup.find("h3")  # (li ul li h3) for music: works too
print(music)
name= soup.select_one("li ul li span") 
print(name)

# key note-----
select -> returns all
select_one -> returns only one

find -> returns only one
find_all -> returns all

'''
