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

#! /usr/bin/env python3

import sys
import urllib.request as req
import urllib.parse as par

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