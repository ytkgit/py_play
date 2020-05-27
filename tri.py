####FUNC1 BEGIN###
"""" simple math """
#This is sample function to showcase power
# import time
# print ("This function shows the powered number you input")
# time.sleep(1)
# x = int(input("Please enter an integer:")) 
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('0')
# else:
#     print(x,"**",x,"=",x**x,"\n")

# time.sleep(1)
# print("OK, Next")
# y=str(input("Please input your favorite word:"))
# print("word count ", len(y))
# print(y,"...Nice!, I like it too")
####FUNC1 END###

####FUNC2 BEGIN###
"""How  the math works"""
# math = int(input("Please input Li\'s Math score:"))
# jap = int(input("Please input Li\'s jap score:"))
# science = int(input("Please input Li\'s science score:"))
# hist = int(input("Please input Li\'s hist score:"))
# total=math+jap+science+hist
# print("Total score of Li is ",total)
# for n in range(2,10):
#     for x in range(2,n):
#         if n % x ==0:
#             print(n,'equals', x,'*',n//x)
#             break
#         else:
#             #loop fell through without finding a factor
#             print(n,'is a prime number')
####FUNC2 END###

####FUNC2 OPTIONS###
# #continue pattern
# for num in range(2,10):
#     if num %2 == 0:
#         print('found an even number', num)
#         continue
#     print('found a number', num)

# #else pattern
# for num in range(2,10):
#     if num %2 == 0:
#         print('found an even number', num)
#     else:
#         print('found a number', num)

# #fobonacci function
# def fib(n):
#     """Print Fibonacci series up to n"""
#     a,b = 0,1
#     while a < n:
#         print(a, end=', ')
#         a,b = b, a+b
#     print()


####FUNC3 BEGIN###
"""This is downloading fuction which fetch the data from the specified URL"""
# import urllib.request
# url = 'http://192.168.33.10/wp-content/uploads/2020/04/fa125c97f7b4281b2959095622154e18.jpg'
# name = 'yane1.jpg'
# #ask before the download
# ans = str(input("Do you want download the image?(input Yes or No): "))
# if ans == "Yes":
#     urllib.request.urlretrieve(url, name)
#     print('saved the image as ', name)

# elif ans == "No":
#     print("Donwload stopped")
####FUNC3 END###

####FUNC4 BEGIN###
# with open("test.txt",mode="x") as f:
#     for i in range(10):
#         x = i**i
#     print(x)


# #get url request
# import urllib.request

# url = "https://api.aoikujira.com/ip/ini"
# res = urllib.request.urlopen(url)
# data = res.read()

# text = data.decode("utf-8")
# print(text)
####FUNC4 END###


###FUNC5 BEGIN###
"""Get the data from the url"""
#import section
import urllib.request
import time

#variable section
url = "http://192.168.33.10/wp-content/uploads/2020/04/f0b3b5c08f768ef5eaf13c596f68ee34-547x1024.jpg"
name = "hashimotokanna1.png"

#control section
print("Downloading the image will begin")
time.sleep(2) 
urllib.request.urlretrieve(url,name)
print("Done")