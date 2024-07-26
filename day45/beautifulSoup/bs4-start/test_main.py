#!/usr/bin/env python

from bs4 import BeautifulSoup


with open("./website.html", "r", encoding="utf-8") as file:
    content = file.read()


soup =BeautifulSoup(content,"html.parser")

print(soup.title.string)

for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.h3.string)

print(soup.find_all('img'))
