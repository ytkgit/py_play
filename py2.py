#! /usr/bin/python
###MOD1 BEGIN###
"""how to use beautifulsoup"""
#1 import library
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par

# #2 target html
# html = """
# <html><body>
#     <h1> what the scraping is</h1>
#     <p1>parsing the html</p1>
#     <p2>to extract the part you want</p2>
# </body></html>
# """
# #3 parse the html
# soup = BeautifulSoup(html,'html.parser')

# #4 extract the text
# h1 = soup.html.body.h1
# p1 = soup.html.body.p1
# p2 = p1.next_sibling.next_sibling

# #5 print the text as output
# print("h1 = ", h1.string)
# print("p1 = ", p1.string)
# print("p2 = ", p2.string)

# ###MOD1 END###

##MOD2 BEGIN###
"""fetch the raw html info as text format"""
#1 define variable
url = str(input("保存したいURLを入力してください : "))

with req.urlopen(url) as r:
    b = r.read()
    data = b.decode("utf-8")
#    print(data)
ans1 = str(input("取得したhtmlの内容をファイルに保存しますか? Y or N : "))

if ans1 == "Y":
    with open("html1.txt", mode="w") as f:
        f.write(data)
        print("保存しました。")
elif ans1 == "N":
    print("保存しませんでした。")
else:
    print("保存しませんでした。")
##MOD2 END###