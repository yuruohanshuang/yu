# 项目目录说明

| 目录 | 主要职责 | 典型内容 |
| --- | --- | --- |
| src/models/ | 描述业务对象 | User、AdminUser、StudentUser |
| src/core/ | 提供项目核心能力 | AppConfig、ConfigFactory、AppError |
| try_user_model.py | 演示用户模型 | 创建和调用用户对象 |
| try_app_core.py | 演示核心模块 | 创建配置、校验配置、捕获异常 |

核心知识

什么是静态方法、类方法：

静态方法（@staticmethod）：写在类内部但不自动接收 self 或 cls 的方法。它本质上是"碰巧放在类里的普通函数"，适合放置与类相关但不依赖任何对象状态的工具逻辑。

类方法（@classmethod）：第一个参数自动绑定为类本身（cls）的方法。它不操作某个具体对象，而是操作类级别的数据或创建对象，常用于"替代构造方法"。

三种方法对比：

# 方法类型说明

| 方法类型 | 第一个参数 | 能访问什么 | 适合场景 | 本课例子 |
| --- | --- | --- | --- | --- |
| 实例方法 | self | 当前对象属性 | 读取或修改当前配置 | get() / set() |
| 静态方法 | 无固定参数 | 不自动访问对象或类 | 独立校验、格式转换 | parse_bool() |
| 类方法 | cls | 类属性、类本身 | 工厂入口、替代构造 | from_dict() |


# 类属性说明

# 类属性说明

| 类属性 | 作用 |
| --- | --- |
| DEFAULTS | 所有配置对象都可以使用的默认配置 |
| REQUIRED_KEYS | 校验时必须存在的配置项 |
| VALID_LOG_LEVELS | 允许的日志级别范围 |

要用当前对象数据 → 实例方法 self

只是工具函数 → 静态方法 @staticmethod

要用类创建对象 → 类方法 @classmethod

class AppConfig:
    """演示类属性、静态方法和类方法."""

    DEFAULTS = {"debug": False, "log_level": "INFO"}
    REQUIRED_KEYS = ["app_name", "debug", "log_level"]
    VALID_LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR"]

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

    @classmethod
    def from_dict(cls, data):
        # return cls(data)
        return AppConfig(data)

什么是 __new__：
__new__ 是 Python 对象创建的核心方法，在 __init__ 之前执行。__init__ 负责初始化对象属性，
而 __new__ 负责真正创建并返回对象本身。
绝大多数类不需要重写 __new__（Python 默认帮你创建），但单例模式通过重写 __new__ 来拦截对象创建过程。

对象创建顺序：
AppConfig()
   │
   ▼
先调用 __new__：负责创建或返回对象
   │
   ▼
再调用 __init__：负责初始化对象属性

# 单例模式属性说明

| 属性 | 作用 |
| --- | --- |
| `_instance` | 保存唯一实例，第一次为空，后续复用 |
| `_initialized` | 标记是否已经初始化，避免重复清空配置 |
| `__new__` | 控制对象创建过程 |
| `__init__` | 初始化配置内容，但只应真正执行一次 |

工厂模式创建不同的环境配置：

概念引入

项目通常有不同运行环境：开发环境、测试环境、生产环境。 这些环境的配置不完全相同：开发环境可能打开调试，测试环境使用内存数据库，生产环境关闭调试。
如果每个调用方都自己判断环境，会造成重复代码。 工厂模式的作用是：把对象创建逻辑集中到一个入口。

核心知识

不同环境配置差异：

# 环境配置说明

| 环境 | debug | log_level | database_url | 使用场景 |
| --- | --- | --- | --- | --- |
| dev | True | DEBUG | sqlite:///dev.db | 本地开发和课堂演示 |
| test | True | DEBUG | sqlite:///:memory: | 自动测试和临时验证 |
| prod | False | INFO | sqlite:///app.db | 模拟正式运行 |



