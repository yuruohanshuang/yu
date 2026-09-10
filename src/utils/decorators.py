"""
decorators - 
Date:2026/9/10
"""
import functools
import time
from src.utils.logger import get_logger


def timer(precision: int = 4):
    """计时装饰器，precision 控制小数位数.

    Args:
        precision: 保留几位小数，默认 4 位.

    Example:
        @timer()
        def slow_func():
            time.sleep(0.3)
        # 输出: slow_func 耗时 0.3012 秒
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = round(time.perf_counter() - start, precision)
            print(f"{func.__name__} 耗时 {elapsed} 秒")
            return result
        return wrapper
    return decorator


# 用法
@timer()
def slow_func():
    time.sleep(0.3)

@timer(precision=2)
def slow_func2():
    time.sleep(0.3)

# slow_func()   # slow_func 耗时 0.3012 秒
# slow_func2()  # slow_func2 耗时 0.30 秒
#

log = get_logger(__name__, "logs/app.log")


def log_calls(func):
    """记录函数调用的参数与返回值到日志.

    Example:
        @log_calls
        def add(a, b):
            return a + b
        # 日志: INFO | 调用 add(args=(1, 2), kwargs={})
        # 日志: INFO | add 返回 3
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        log.info("调用 %s(args=%s, kwargs=%s)", func.__name__, args, kwargs)
        result = func(*args, **kwargs)
        log.info("%s 返回 %s", func.__name__, result)
        return result
    return wrapper


# 用法
@log_calls
def add(a, b):
    return a + b

# add(3, 5)
# INFO | 调用 add(args=(3, 5), kwargs={})
# INFO | add 返回 8

def retry(max_attempts: int = 3, delay: float = 1.0,
          exceptions: tuple = (Exception,)):
    """重试装饰器：失败时按 delay 间隔重试，超出 max_attempts 抛出最后一次异常."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_err = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_err = e
                    print(f"[retry] {func.__name__} 第 {attempt} 次失败: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            if last_err is not None:
                raise last_err
            raise RuntimeError("未知错误")  # last_err 为 None 时的兜底

        return wrapper

    return decorator


@retry(max_attempts=3, delay=0.2, exceptions=(ConnectionError,))
def unstable_call(n):
    """模拟不稳定的 API 调用."""
    import random
    if random.random() < 0.7:
        raise ConnectionError("网络抖动")
    return f"成功 n={n}"


# print(unstable_call.__name__)   # unstable_call ← 因为用了 @wraps
# print(unstable_call.__doc__)    # 模拟不稳定的 API 调用. ← 元信息保留
