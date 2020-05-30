#! /usr/bin/python
###MOD1 BEGIN###
"""input 7 digit and search the detail of the place"""

#1 import library
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par

#2 variables
zipcode = str(input("住所の7桁を入力してください :"))

#3 parse the html
url = str("https://api.aoikujira.com/zip/xml/"+ zipcode)
with req.urlopen(url) as r:
    b = r.read()
    data = b.decode("utf-8")
#    print(data)

soup = BeautifulSoup(data,'html.parser')

#4 extract the data
disp = soup.find("disp").string
#shi = soup.find("shi").string
#cho = soup.cho("cho").string
print(disp)