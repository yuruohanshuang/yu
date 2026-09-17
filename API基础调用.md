# URL基础调用

import requests

url = "https://jsonplaceholder.typicode.com/users/1"
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers, timeout=10)
user = response.json()

print(response.status_code)
print(user["name"])
print(user["email"])



# API 工具与 requests 对应关系

| 工具中的概念 | requests 中的写法 | 说明 |
| --- | --- | --- |
| Method = GET | `requests.get(url)` | 发送查询请求 |
| Method = POST | `requests.post(url)` | 发送创建或提交请求 |
| URL | `url` 参数 | 请求目标地址 |
| Params | `params={...}` | URL 查询参数 |
| Headers | `headers={...}` | 请求头 |
| Body raw JSON | `json={...}` | JSON 请求体 |
| Status | `response.status_code` | 响应状态码 |
| Response Body | `response.text` / `response.json()` | 响应内容 |

# requests 请求常用写法

| 场景 | 写法 | 说明 |
| --- | --- | --- |
| 查询详情 | `requests.get(url)` | URL 已经包含完整路径 |
| 查询列表 | `requests.get(url, params=params)` | 查询参数交给 `params` |
| 添加请求头 | `requests.get(url, headers=headers)` | 传递 `Accept`、`Authorization` 等 |
| 设置超时 | `requests.get(url, timeout=10)` | 避免程序长时间卡住 |

# Response 对象常用属性与方法

| 属性 / 方法 | 含义 | 常用场景 |
| --- | --- | --- |
| `status_code` | HTTP 状态码 | 判断请求是否成功 |
| `url` | 最终请求 URL | 检查 `params` 是否拼接正确 |
| `headers` | 响应头 | 查看 `Content-Type` |
| `text` | 文本响应体 | 查看原始文本 |
| `json()` | JSON 解析结果 | API 数据处理 |
| `elapsed` | 请求耗时 | 观察接口响应速度 |

# POST     常用请求参数

| 参数 | 作用 | 典型场景 |
| --- | --- | --- |
| `json` | 发送 JSON 请求体 | API 创建资源、提交结构化数据 |
| `data` | 发送表单数据 | 表单提交 |
| `headers` | 设置请求头 | `Accept`、`Authorization`、自定义头 |
| `timeout` | 设置超时时间 | 防止请求长时间无响应 |

# data 与 json 的区别

| 写法 | Content-Type | 服务端看到的数据 | 使用建议 |
| --- | --- | --- | --- |
| `data={...}` | `application/x-www-form-urlencoded` | 表单字段 | 网页表单场景 |
| `json={...}` | `application/json` | JSON 对象 | API 调用优先使用 |

# 常用请求头 Header

| Header | 示例 | 说明 |
| --- | --- | --- |
| `Accept` | `application/json` | 希望返回 JSON |
| `Content-Type` | `application/json` | 请求体是 JSON |
| `Authorization` | `Bearer <YOUR_API_KEY>` | 认证信息，真实值不要写进课件 |

# requests 与 requests.Session 对比

| 维度 | 直接 `requests` | `requests.Session` |
| --- | --- | --- |
| TCP 连接 | 每次新建 | 复用（HTTP Keep-Alive） |
| Cookie | 手动管理 | 自动保存和发送 |
| 默认 Header | 每次传 | `session.headers.update()` 统一设置 |
| 适用场景 | 一次性请求 | 同一域名多次请求 |
