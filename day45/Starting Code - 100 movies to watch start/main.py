#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")
print(soup.title.getText())

data = soup.find_all(name="h3",class_="title")

titles = [title.getText().encode("utf-8") for title in data]


reversed_copy = titles[::-1]

movie_data =""

for movie in reversed_copy:
    movie_data += f"{movie}\n"

with open("./top100movies.txt", "w") as file:
    file.write(movie_data)

print("100 top movies file was created successfully!!!")

