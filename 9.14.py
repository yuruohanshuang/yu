"""
9.14 - 
Date:2026/9/14
"""
from wsgiref.headers import Headers

"""
Method: GET
URL: https://jsonplaceholder.typicode.com/users/1
Header:
  Accept: application/json

import requests

url = "https://jsonplaceholder.typicode.com/users/1"
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers, timeout=10)
user = response.json()

print(response.status_code)
print(user["name"])
print(user["email"])




Method: GET
URL: https://jsonplaceholder.typicode.com/posts/1
Header:
  Accept: application/json

"""
import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"
# Headers = {"Accept":"application/json"}
# response = requests.get(url, headers=Headers, timeout=10)
# data = response.json()
# #
# # print(response.status_code)
# # print(data["body"])
#
# print(requests.__version__)

# url = "https://jsonplaceholder.typicode.com/posts"
# params = {
#     "userId": 1,
#     "_limit": 5,
# }
#
# response = requests.get(url, params=params, timeout=10)
# posts = response.json()

# print("最终 URL:", response.url)
# print("状态码:", response.status_code)
# print("文章数量:", len(posts))
# print("第一篇标题:", posts[0]["title"])
# print("响应头:", response.headers)
# print("响应体:", response.text)
# print("解析后的 JSON 数据:", response.json())
# print("请求耗时:", response.elapsed)

# url = "https://jsonplaceholder.typicode.com/posts"
# params = {"userId": 2 ,"_limit": 3 }
#
# response = requests.get(url, params = params , timeout = (5,30))
# posts = response.json()

# response = client.get("https://jsonplaceholder.typicode.com/users/1")

# 方式 1：dict.get() 链式取值
# company = response.get("company", {})
# name = company.get("name", "未知")

# 方式 2：多层嵌套时逐层取值
# data = response.json()
#
# data = data.json("data", {})
# user = data.json("user", {})
# profile = user.json("profile", {})
# name = profile.json("name", "未知")
# print(name)
# for post in posts:
#     print(post["id"],post["title"])

# 连接超时 5 秒，读取超时 30 秒

# 创建文章
# url = "https://jsonplaceholder.typicode.com/posts"
# payload = {
#     "title": "Day10 API 基础调用",
#     "body": "使用 requests 发送 POST JSON 请求",
#     "userId": 1,
# }
# headers = {"Accept": "application/json"}
#
# response = requests.post(url, json=payload, headers=headers, timeout=10)
# result = response.json()
#
# print("状态码:", response.status_code)
# print("新资源 ID:", result.get("id"))
# print("标题:", result.get("title"))

#对比data和json的区别
# url = "https://httpbin.org/post"
# body = {"name": "student", "role": "api learner"}
#
# form_response = requests.post(url, data=body, timeout=10)
# json_response = requests.post(url, json=body, timeout=10)
#
# print("form:", form_response.json().get("form"))
# print("json:", json_response.json().get("json"))

#url = "https://jsonplaceholder.typicode.com/posts"
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title":"课堂练习",
    "body":"练习POST JSON请求",
    "userId":3,
}

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer <YOUR_API_KEY>",  # 真实值从 .env 读取
}

response = requests.post(url, json=data, headers=headers, timeout=10)
print("状态码:", response.status_code)
print("新资源 ID:", response.json())


# requests.Session：自动管理 Cookie 与连接复用
session = requests.Session()
session.headers.update({"Accept": "application/json"})

# 第一次请求
r1 = session.get("https://jsonplaceholder.typicode.com/users/1", timeout=10)
print(r1.json()["name"])

# 第二次请求复用同一个 TCP 连接
r2 = session.get("https://jsonplaceholder.typicode.com/users/2", timeout=10)
print(r2.json()["name"])

# 用完关闭
session.close()

