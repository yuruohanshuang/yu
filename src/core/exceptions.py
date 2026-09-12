"""
exceptions - 
Date:2026/9/11
"""

class AppError(Exception):
    """应用异常基类."""

    def __init__(self, message, error_code="APP_ERROR"):
        self.message = message
        self.error_code = error_code
        super().__init__(message)

    def __str__(self):
        return f"[{self.error_code}] {self.message}"


class ConfigError(AppError):
    """配置错误."""

    def __init__(self, message):
        super().__init__(message, "CONFIG_ERROR")


class ValidationError(AppError):
    """数据校验错误."""

    def __init__(self, field, reason):
        message = f"字段 {field} 校验失败: {reason}"
        super().__init__(message, "VALIDATION_ERROR")


class APIError(AppError):
    """API 调用错误."""

    def __init__(self, url, status_code, response_data):
        message = f"API 调用失败: {url}, 状态码={status_code}, 返回内容={response_data}"
        super().__init__(message, "API_ERROR")


class DatabaseError(AppError):
    """数据库错误."""
    def __init__(self, operation,reason):
        message = f"数据库操作{operation}失败: {reason}"
        super().__init__(message, "DATABASE_ERROR")


try:
    raise DatabaseError("SELECT", "数据库连接超时")
except AppError as e:
    print(e.error_code)
    print(e)