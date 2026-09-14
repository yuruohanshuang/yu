"""
client - 
Date:2026/9/14
"""

import requests

from src.core import APIError
from src.utils.decorators import retry

import requests
import logging

from src.core import APIError, ResourceNotFoundError, AuthError, ServerError

logger = logging.getLogger(__name__)


class APIClient:
    """基础 API 调用客户端（Session 版本）."""

    def __init__(self, base_url, timeout=10, headers=None):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(headers or {"Accept": "application/json"})

    def _build_url(self, path):
        return f"{self.base_url}/{path.lstrip('/')}"

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
            raise APIError("响应不是有效 JSON", "API_ERROR", str(e))
        # 业务码双层校验
        if isinstance(data, dict) and "code" in data and data.get("code") != 0:
            from src.core import ValidationError
            raise ValidationError("业务", data.get("message", "业务处理失败"))
        return data

    def get(self, path, params=None):
        url = self._build_url(path)
        response = self.session.get(url, params=params, timeout=self.timeout)
        return self._handle_response(response)

    def post(self, path, json_data=None):
        url = self._build_url(path)
        response = self.session.post(url, json=json_data, timeout=self.timeout)
        return self._handle_response(response)

    def put(self, path, json_data=None):
        """完整更新资源."""
        url = self._build_url(path)
        response = self.session.put(url, json=json_data, timeout=self.timeout)
        return self._handle_response(response)

    def delete(self, path):
        """删除资源."""
        url = self._build_url(path)
        response = self.session.delete(url, timeout=self.timeout)
        return self._handle_response(response)

    def close(self):
        """关闭 Session，释放连接."""
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()