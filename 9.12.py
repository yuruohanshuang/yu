"""
9.12 - 
Date:2026/9/11
"""
import json

# JSON 字符串 -> Python 字典（Day10 API 响应解析会用到）
text = '{"name": "小明", "age": 18}'
data = json.loads(text)
print(data["name"])  # 小明

# Python 字典 -> JSON 字符串（Day10 发送请求体时会用到）
payload = {"title": "测试", "body": "hello"}
text = json.dumps(payload, ensure_ascii=False)
print(text)  # {"title": "测试", "body": "hello"}
