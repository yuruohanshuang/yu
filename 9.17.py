"""
9.17 - 
Date:2026/9/17
"""
import requests
#
# URL = "https://jsonplaceholder.typicode.com/posts"
# headers = {"Accept": "application/json"}
#
# response = requests.get(URL, headers=headers, timeout=10, params={"userId": 1, "_limit": 5})
# posts = response.json()
#
# for post in posts:
#     print(f"title: {post['title']}")

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title":"测试文章",
    "body":"测试文章内容",
    "userId": 1
}

response = requests.post(url, json=data)

print("状态码:", response.status_code)

result = response.json()
print("新资源ID:",result["id"])
