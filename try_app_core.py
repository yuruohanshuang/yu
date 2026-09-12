"""
try_app_core - 
Date:2026/9/12
"""

from src.core import AppConfig, ConfigFactory, AppError, ConfigError, ValidationError, APIError, DatabaseError

def show_config(env: str):
    config = ConfigFactory.create(env)
    print(f"Environment: {env}环境")
    print(config.to_dict())


try:
    show_config("dev")
    show_config("test")
    show_config("prod")

    config1 = AppConfig()
    config2 = AppConfig()
    print(f"\nconfig1 is config2: {config1 is config2}")

    try:
        ConfigFactory.create("unknown")
    except ConfigError as e:
        print(f"\n捕获配置异常: {e.error_code} - {e}")

except AppError as e:
    print(f"应用异常: {e.error_code} - {e}")