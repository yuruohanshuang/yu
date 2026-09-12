"""
config - 
Date:2026/9/11
"""
import json
from pathlib import Path
from typing import Any

from src.core.exceptions import ConfigError

class AppConfig:
    """演示类属性、静态方法和类方法."""

    DEFAULTS = {"api_timeout": 30, "debug": False, "log_level": "INFO", "app_name": "AI学习平台"}
    REQUIRED_KEYS = ["app_name", "debug", "log_level"]
    VALID_LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR"]
    VALID_ENVS = ["dev","test","prod"]
    _instance = None  # 私有类属性，用于存储类的唯一实例
    _initialized = False  # 私有类属性，用于标识类是否已初始化

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if AppConfig._initialized:
            return
        self._config = {
            "app_name": "AI学习平台",
            "debug": False,
            "log_level": "INFO",
        }
        AppConfig._initialized = True

    def get(self, key, default=None):
        return self._config.get(key, default)

    def set(self, key, value):
        self._config[key] = value

    def load_from_dict(self, data: dict):
        self._config.update(data)

    def load_from_file(self, filepath: str):
        try:
            path = Path(filepath)

            if not path.exists():
                raise ConfigError(f"配置文件不存在: {filepath}")
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)


            self.load_from_dict(data)

        except json.JSONDecodeError:
            raise ConfigError(f"配置文件格式错误: {filepath}")


    @staticmethod
    def parse_bool(value):
        return str(value).lower() in ["true", "1", "yes"]

    @staticmethod
    def is_valid_log_level(level):
        return level in AppConfig.VALID_LOG_LEVELS

    @classmethod
    def from_dict(cls, data: dict):
        config = cls()
        config.load_from_dict(data)
        return config

    def validate(self):
        for key in self.REQUIRED_KEYS:
            if key not in self._config:
                raise ConfigError(f"缺少必填配置项: {key}")
        if not self.is_valid_log_level(self.get("log_level")):
            raise ConfigError(f"无效日志级别: {self.get('log_level')}")

        if self.get("api_timeout") is None:
            raise ConfigError(f"缺少必填配置项: api_timeout")

    def to_dict(self) -> dict:
        return self._config.copy()

class ConfigFactory:
    """配置工厂：统一创建不同环境配置."""


    @staticmethod
    def create(env: str) -> AppConfig:
        AppConfig._instance = None
        AppConfig._initialized = False

        configs = {
            "dev": {"app_name": "AI学习平台-开发环境", "debug": True, "log_level": "DEBUG","api_timeout": 30},
            "test": {"app_name": "AI学习平台-测试环境", "debug": True, "log_level": "DEBUG","api_timeout": 30},
            "prod": {"app_name": "AI学习平台", "debug": False, "log_level": "INFO","api_timeout": 30},
            "local": {"app_name": "AI学习平台-本地环境", "debug": True, "log_level": "DEBUG","api_timeout": 30},
        }

        if env not in configs:
            raise ConfigError(f"不支持的环境: {env}")

        config = AppConfig.from_dict(configs[env])
        config.validate()
        return config

class LoggerFactory:
    """日志工厂"""

    @staticmethod
    def create(log_level):

        loggers = {

            "DEBUG": lambda msg:
                print(f"[DEBUG] {msg}"),

            "INFO": lambda msg:
                print(f"[INFO] {msg}"),

            "ERROR": lambda msg:
                print(f"[ERROR] {msg}")

        }

        if log_level not in loggers:
            raise ConfigError(
                f"不支持日志级别: {log_level}"
            )

        return loggers[log_level]
# config = AppConfig.from_dict({
#     "app_name": "AI学习平台",
#     "debug": AppConfig.parse_bool("true"),
#     "log_level": "DEBUG",
# })
#
# print(config.get("app_name"))
# print(AppConfig.is_valid_log_level(config.get("log_level")))
# config1 = AppConfig()
# config2 = AppConfig()
#
# config1.set("app_name", "课堂演示")
#
# print(config1 is config2)
# print(config2.get("qpp_name"))

if __name__ == "__main__":
    config =  ConfigFactory.create("local")
    print(config.get("database_url"))
    logger = LoggerFactory.create("DEBUG")

    logger("开始加载配置")
#     for env in ["dev", "test", "prod"]:
#         config = ConfigFactory.create(env)
#         print(env, config.get("app_name"), config.get("debug"))