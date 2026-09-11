"""
AppConfig - 
Date:2026/9/11
"""
class AppConfig:
    """演示类属性、静态方法和类方法."""

    DEFAULTS = {"debug": False, "log_level": "INFO", "app_name": "AI学习平台"}
    REQUIRED_KEYS = ["app_name", "debug", "log_level"]
    VALID_LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR"]
    VALID_ENVS = ["dev","test","prod"]


    def __init__(self, config_data=None):
        self._config = self.DEFAULTS.copy()
        if config_data:
            self._config.update(config_data)

    def get(self, key, default=None):
        return self._config.get(key, default)

    def set(self, key, value):
        self._config[key] = value

    @staticmethod
    def parse_bool(value):
        return str(value).lower() in ["true", "1", "yes"]

    @staticmethod
    def is_valid_log_level(level):
        return level in AppConfig.VALID_LOG_LEVELS

    @staticmethod
    def is_valid_env(env):
        return env in AppConfig.VALID_ENVS

    @classmethod
    def create_default(cls):
        return cls(cls.DEFAULTS)

    @classmethod
    def from_dict(cls, data):
        # return cls(data)
        return AppConfig(data)

config = AppConfig.from_dict({
    "app_name": "AI学习平台",
    "debug": AppConfig.parse_bool("true"),
    "log_level": "DEBUG",
})

print(config.get("app_name"))
print(AppConfig.is_valid_log_level(config.get("log_level")))