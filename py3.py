#! /usr/bin/python
###MOD1 BEGIN###
"""input the url and parse the html"""

#1 import library
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par

#1 variables
url = str(input("解析したいURLを入力してください :"))

#2 parse the html
with req.urlopen(url) as r:
    b = r.read()
    data = b.decode("utf-8")

soup = BeautifulSoup(data,'html.parser')

#3 find all method
links = soup.find_all("a")

#4 show links
for a in links:
    href = a.attrs["href"]
    text = a.string
    print(text," > ",href)

#5 list the video content
li_list = soup.select("div#entry-content > figure.wp-block-video > video")
for li in li_list:
    print("li = ",li.string)
###MOD1 END###