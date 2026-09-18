"""
client - 
Date:2026/9/14
"""

import requests
from sockshandler import merge_dict

from src.core import APIError
from src.utils.decorators import retry


import requests
import logging

from src.core import APIError, ResourceNotFoundError, AuthError, ServerError

logger = logging.getLogger(__name__)

@retry(max_attempts=3, exceptions=(APIError, ServerError))
class APIClient:
    """基础 API 调用客户端（Session 版本）."""

    def __init__(self, base_url, timeout=10, headers=None):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(headers or {"Accept": "application/json"})

        if headers:
            self.session.headers.update(headers)
    def _build_url(self, path):
        return f"{self.base_url}/{path.lstrip('/')}"

    def set_token(self, token):
        self.session.headers.update({
            "Authorization": f"Bearer {token}"
        })

    def _raise_for_status(self, response):
        """根据 HTTP 状态码分发到具体异常子类."""
        status = response.status_code
        if 200 <= status < 300:
            return
        if status == 400:
            from src.core import ValidationError
            raise ValidationError("请求", f"参数错误 (HTTP {status})")
        elif status == 401:
            from src.core import AuthError
            raise AuthError()
        elif status == 403:
            from src.core import PermissionError
            raise PermissionError()
        elif status == 404:
            raise ResourceNotFoundError(response.url)
        elif status == 429:
            from src.core import RateLimitError
            retry_after = response.headers.get("Retry-After", "0")
            raise RateLimitError(int(retry_after))
        elif status >= 500:
            raise ServerError(status)
        else:
            raise APIError(f"API 请求失败 (HTTP {status})", "API_ERROR")

    def _handle_response(self, response):
        self._raise_for_status(response)
        try:
            data = response.json()
        except ValueError as e:
            raise APIError("响应不是有效 JSON",
                           "API_ERROR",
                           str(e)) from e
        # 业务码双层校验
        if isinstance(data, dict) and "code" in data and data.get("code") != 0:
            from src.core import ValidationError
            raise ValidationError("业务",
            data.get("message", "业务处理失败"))
        return data

    def _merge_headers(self, headers = None):
        """合并默认header和单次请求header"""
        merge_headers = dict(self.session.headers)
        if headers:
            merge_headers.update(headers)
        return merge_headers

    def get(self, path, params=None, headers=None):
        """发送 GET 请求."""
        url = self._build_url(path)
        merged_headers = self._merge_headers(headers)

        response = self.session.get(
            url,
            params=params,
            headers=merged_headers,
            timeout=self.timeout
        )
        return self._handle_response(response)

    def post(self, path, json_data=None, headers=None):
        """发送 POST 请求."""
        url = self._build_url(path)
        merged_headers = self._merge_headers(headers)

        response = self.session.post(
            url,
            json=json_data,
            headers=merged_headers,
            timeout=self.timeout
        )
        return self._handle_response(response)

    def put(self, path, json_data=None, headers=None):
        """完整更新资源."""
        url = self._build_url(path)
        merged_headers = self._merge_headers(headers)

        response = self.session.put(
            url,
            json=json_data,
            headers=merged_headers,
            timeout=self.timeout
        )
        return self._handle_response(response)

    def delete(self, path, headers=None):
        """删除资源."""
        url = self._build_url(path)
        merged_headers = self._merge_headers(headers)

        response = self.session.delete(
            url,
            headers=merged_headers,
            timeout=self.timeout
        )
        return self._handle_response(response)

    def close(self):
        """关闭 Session，释放连接."""
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

if "__name__" == "__main__":
    client = APIClient(
        base_url="https://api.example.com",
        headers={
            "Authorization": "Bearer token123",
            "Content-Type": "application/json"
        }
    )

    # 使用默认 Header
    client.get("/students")

    # 单次请求新增 Header
    client.get(
        "/students",
        headers={"X-Request-ID": "req-001"}
    )

    # 单次请求覆盖默认 Authorization
    client.get(
        "/students",
        headers={"Authorization": "Bearer new_token"}
    )