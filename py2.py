#! /usr/bin/python3
###MOD1 BEGIN###
"""how to use beautifulsoup"""
#1 import library
from bs4 import Beautifulsoup

#2 target html
html = """
<html><body>
    <h1> what the scraping is</h1>
    <p1>parsing the html</p1>
    <p2>to extract the part you want</p2>
</body></html>
"""
#3 parse the html
soup = Beautifulsoup(html,'html.parser')

#4 extract the text
h1 = soup.html.body.h1
p1 = soup.html.body.p1
p2 = p1.next_sibling.next_sibling

#5 print the text as output
print("h1 = ", h1.string)
print("p1 = ", p1.string)
print("p2 = ", p2.string)

###MOD1 END###