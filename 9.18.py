# import urllib.request
#
# response = urllib.request.urlopen("http://www.baidu.com")
# html = response.read()
# print(html.decode('utf-8'))
from tarfile import ReadError

# requests模块
import requests
from requests import ConnectTimeout, ReadTimeout

#
# response = requests.get("http://www.baidu.com") #对需要爬取的网站发送请求
# print('状态码:', response.status_code) #打印状态码
# print('url:',response.url) #打印url
# print('响应头:', response.headers) #打印响应头
# print("cookie", response.cookies) #打印cookie
# print('响应内容:', response.text) #以文本形式打印出网页源码
# print("content",response.content) #以字节形式打印出网页源码

# 以post方式发送请求
data ={'kw':'苹果'}
response = requests.post("https://fanyi.baidu.com/s", data=data)
print(response.content)


# 传递URL参数
# 介绍：在发送请求时，可以通过params参数传递URL查询参数

params = {'wd': 'Python'}
response = requests.get("https://www.baidu.com/s", params=params)
print(response.url)
print(response.status_code)


# 传递请求头
# 介绍：在发送请求时，有时可能会出现需要传递自定义请求头的情况，可以通过headers参数实现
# 请求头中有很多内容，其中最常用的就是User-Agent和Host
# User-Agent是浏览器的身份标识，Host是请求的主机名

headers = {'User-Agent': 'Mozilla/5.0',"host":"www.baidu.com"}
response = requests.get("https://www.baidu.com", headers=headers)
print(response.headers)

#网络超时
# 介绍：在发送请求时，有时可能会出现网络超时的情况，可以通过timeout参数实现
try:
    response = requests.get("https://www.baidu.com", timeout=1)
    print(response.status_code)
except ReadTimeout or ConnectTimeout:
    print("The request timed out")
