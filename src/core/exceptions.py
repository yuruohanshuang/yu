"""
exceptions - 
Date:2026/9/11
"""
"""API 异常定义及 HTTP 状态码映射."""

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
        super().__init__(f"字段 {field} 校验失败: {reason}", "VALIDATION_ERROR")


class DatabaseError(AppError):
    """数据库错误."""

    def __init__(self, operation, reason):
        super().__init__(f"数据库操作{operation}失败: {reason}", "DATABASE_ERROR")


class APIError(AppError):
    """API 调用错误."""

    def __init__(self, url, status_code, response_data=None, message=None):
        self.url = url
        self.status_code = status_code
        self.response_data = response_data
        detail = message or f"API 调用失败: {url}, 状态码={status_code}, 返回内容={response_data}"
        super().__init__(detail, "API_ERROR")


class BadRequestError(APIError):
    """请求参数错误（400）."""

    def __init__(self, url, status_code=400, response_data=None):
        super().__init__(url, status_code, response_data, "请求参数错误")


class AuthError(APIError):
    """认证失败（401）."""

    def __init__(self, url, status_code=401, response_data=None):
        super().__init__(url, status_code, response_data, "认证失败")


class ForbiddenError(APIError):
    """无权访问（403）."""

    def __init__(self, url, status_code=403, response_data=None):
        super().__init__(url, status_code, response_data, "无权访问该资源")


class ResourceNotFoundError(APIError):
    """资源不存在（404）."""

    def __init__(self, url, status_code=404, response_data=None):
        super().__init__(url, status_code, response_data, "请求的资源不存在")


class ConflictError(APIError):
    """资源冲突（409）."""

    def __init__(self, url, status_code=409, response_data=None):
        super().__init__(url, status_code, response_data, "请求发生资源冲突")


class RateLimitError(APIError):
    """请求过于频繁（429）."""

    def __init__(self, url, status_code=429, response_data=None):
        super().__init__(url, status_code, response_data, "请求过于频繁，已触发速率限制")


class ServerError(APIError):
    """服务器错误（5xx）."""

    def __init__(self, url, status_code=500, response_data=None):
        super().__init__(url, status_code, response_data, "服务器内部错误")


# 8 个具体 APIError 子类的状态码映射
STATUS_CODE_EXCEPTION_MAP = {
    400: BadRequestError,
    401: AuthError,
    403: ForbiddenError,
    404: ResourceNotFoundError,
    409: ConflictError,
    429: RateLimitError,
    500: ServerError,
    503: ServerError,
}


def raise_for_status_code(url, status_code, response_data=None):
    """根据 HTTP 状态码抛出对应异常；未配置的错误状态码使用 APIError。"""
    if status_code < 400:
        return

    exception_class = STATUS_CODE_EXCEPTION_MAP.get(status_code, APIError)
    raise exception_class(url, status_code, response_data)