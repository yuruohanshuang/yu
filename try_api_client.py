"""
try_api_client - 
Date:2026/9/14
"""

from src.api import APIClient
from src.core import APIError

with APIClient("https://jsonplaceholder.typicode.com") as client:
    users = client.get("/users", params={"_limit": 3})
    print(users[0]["name"])

    post = client.post("/posts", json_data={"title": "demo", "body": "hello", "userId": 1})
    print(post.get("id"))