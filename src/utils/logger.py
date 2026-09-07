# src/utils/logger.py
"""项目统一日志工具.

使用方式：
    from src.utils.logger import get_logger
    log = get_logger(__name__, "logs/app.log")
    log.info("启动完成")
"""
import logging
import sys
from pathlib import Path

_FORMAT = "%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s"
_DATEFMT = "%Y-%m-%d %H:%M:%S"


def get_logger(name: str, log_file: str | None = None,
               level: int = logging.INFO) -> logging.Logger:
    """获取一个配置好的 logger 实例.

    Args:
        name: logger 名称，建议传 __name__.
        log_file: 日志文件路径，None 表示只输出到控制台.
        level: 日志级别，默认 INFO.

    Returns:
        已挂载控制台与文件 handler 的 Logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 避免重复添加 handler
    if logger.handlers: #避免重复打印
        return logger

    formatter = logging.Formatter(_FORMAT, datefmt=_DATEFMT)

    # 控制台
    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)
    logger.addHandler(console)

    # 文件
    if log_file:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        file_h = logging.FileHandler(log_file, encoding="utf-8")
        file_h.setFormatter(formatter)
        logger.addHandler(file_h)

    return logger


if __name__ == "__main__":
    log = get_logger("demo", "logs/app.log", level=logging.DEBUG)
    log.debug("调试信息")
    log.info("程序启动")
    log.warning("注意潜在问题")
    log.error("发生错误")