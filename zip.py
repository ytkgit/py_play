#! /usr/bin/python3
###practice for python coding###
import sys
import urllib.request as req
import urllib.parse as par
import requests

###FUNC1 BEGIN###
"""zip code search function"""
# import urllib.request
# import urllib.parse

# API = "https://api.aoikujira.com/zip/xml/get.php"
# code = int(input("What\'s your zip code? input 7 code: "))
# values = {
#     'fmt' : 'json',
#     'zn' : code
# }
# params = urllib.parse.urlencode(values)

# url = API + "?" + params
# print("url=", url)


# data = urllib.request.urlopen(url).read()
# text = data.decode("utf-8")
# print(text)
###FUNC1 END###

###FUNC2 BEGIN###
# if len(sys.argv) <= 1:
#     print("USAGE: zip.py (keyword)")
#     sys.exit()
# keyword = sys.argv[1]

keyword = str(input("知っている和歌の句を入力してみてください。 : "))
API = "https://api.aoikujira.com/hyakunin/get.php"
query = {
    "fmt": "ini",
    "key": keyword
}

params = par.urlencode(query)
url = API + "?" + params
print("url=", url)

with req.urlopen(url) as r:
    b = r.read()
    data = b.decode("utf-8")
    print(data)

if data == "":
    print("該当なし")
else:
    ct = data.count("item")
    print("該当の和歌",ct,"歌")
###FUNC2 END###

###FUNC3 BEGIN###
# """get the full http response
#    usage: put URL into the ()of requests.get
# """
# with open("raw1.txt", mode="w") as f:
#     w = requests.get("https://hpjav.tv/128246/fc2ppv_1321451-b")
#     f.write(w.text)
###FUNC3 END###