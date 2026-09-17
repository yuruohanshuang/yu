"""
APIClient - 
Date:2026/9/17
"""
class APIClient:
    """基础 API 调用客户端（Session 版本）."""
    def __init__(self):
        from src.core.config import AppConfig
        config = AppConfig()
        self.base_url = config.API_BASE_URL
        self.timeout = config.API_TIMEOUT
        self.api_key = config.API_KEY
        self.retry_times = config.API_RETRY_TIMES

    def __set_token(self):


    def _build_url(self, path):


    def _merge_headers(self, headers):
        """合并默认请求头和自定义请求头."""

    def _request(self, method, path, params=None, data=None, headers=None):
        """发送 HTTP 请求并处理响应."""

    def _handle_response(self, response):
        """处理 HTTP 响应."""

    def get(self, path, params=None, headers=None):
        """发送 GET 请求."""

    def post(self, path, json_data=None, headers=None):
        """发送 POST 请求."""

    def put(self):

    def delete(self):


