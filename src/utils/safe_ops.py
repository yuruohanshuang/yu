# src/utils/safe_ops.py
from logger import get_logger

log = get_logger(__name__, "logs/app.log")


def safe_divide(a: float, b: float) -> float | None:
    """安全除法，返回结果或 None."""
    try:
        return a / b
    except ZeroDivisionError:
        log.error("除零错误: %s / %s", a, b)
        return None
    except TypeError as e:
        log.error("类型错误: %s", e)
        return None


def safe_read(path: str) -> str | None:
    """安全读文件，返回内容或 None."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        log.error("文件不存在: %s", path)
        return None

from logger import get_logger
log = get_logger(__name__, "logs/app.log")