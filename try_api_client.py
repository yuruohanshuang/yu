"""
try_api_client - 
Date:2026/9/14
"""

from src.api import APIClient
from src.core import APIError
import os
from dotenv import load_dotenv

load_dotenv()

client = APIClient("https://httpbin.org")
client.set_token("<YOUR_ACCESS_TOKEN>")
result = client.get("/headers")
print(result["headers"].get("Authorization"))