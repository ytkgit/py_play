import inspect
import urllib.request

x= str(input("これから画像を取得します。よろしいですか？　Y or N"))

if x == "Y":
    url = "http://192.168.33.80/wp-content/uploads/2020/04/idl_OoC9_147_452-1-scaled.jpg"
    name = "ikutanana.jpg"
    urllib.request.urlretrieve(url, name)
else:
    pass


