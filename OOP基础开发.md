OOP = 用“对象”把一组相关数据和操作这组数据的方法放在一起

| 现实世界 | OOP 概念 | 本课案例 |
| :--- | :--- | :--- |
| 用户类型 | 类（Class） | `User` 类 |
| 张三这个用户 | 对象 / 实例（Object / Instance） | `User("zhangsan", ...)` |
| 用户名、邮箱、状态 | 属性（Attribute） | `username` / `email` / `is_logged_in` |
| 登录、退出、查看资料 | 方法（Method） | `login()` / `logout()` / `get_profile()` |
类的构造格式
User 对象
├── 数据：username / email / is_logged_in
└── 行为：login() / logout() / get_profile()

| 组成 | 写法 | 作用 |
| :--- | :--- | :--- |
| 类定义 | `class User:` | 声明一个类模板 |
| 构造方法 | `def __init__(self, ...)` | 创建对象时初始化属性 |
| 当前对象 | `self` | 在类内部访问当前对象 |
| 实例属性 | `self.username = username` | 保存每个对象自己的数据 |
| 实例化 | `user = User(...)` | 按类模板创建对象 |



| 类型 | 定义位置 | 访问方式 | 是否共享 | 适用场景 |
| :--- | :--- | :--- | :--- | :--- |
| 类属性 | 类体中，方法外 | `类名.属性` | 所有对象共享 | 平台名、计数器、默认配置 |
| 实例属性 | `__init__` 或方法中 | `对象.属性` / `self.属性` | 每个对象独立 | 用户名、邮箱、登录状态 |
所有对象都一样 → 类属性
每个对象不一样 → 实例属性
class User:
    """演示类属性与实例属性."""
    
    类属性：
    platform_name = "AI学习平台"
    total_count = 0
        
    def __init__(self, username: str, email: str):
        实例属性：
        self.username = username
        self.email = email
        self.is_logged_in = False
        User.total_count += 1

    def show_info(self):
        print(f"平台={User.platform_name}, 用户={self.username}, 邮箱={self.email}")

封装：
即将方法写在类内部，外界直接调用方法

| 原则 | 说明 | 示例 |
| :--- | :--- | :--- |
| 方法名表达动作 | 看名字知道它做什么 | `login()` / `logout()` |
| 状态修改放内部 | 外部只调用方法 | `user.login()` |
| 方法内部做校验 | 不让非法数据进入对象 | `update_email()` |
| 返回结果可判断 | 成功 / 失败明确 | `return True / False` |


封装前：外部代码到处改 user 字典或属性
封装后：外部只调用 user.login() / user.update_email(...)

class User:
    """把状态修改封装到对象方法中."""

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.is_logged_in = False
        self.is_active = True

    def login(self) -> bool:
        if not self.is_active:
            print(f"用户 {self.username} 已被禁用，无法登录")
            return False
        self.is_logged_in = True
        print(f"用户 {self.username} 登录成功")
        return True

    def logout(self):
        self.is_logged_in = False
        print(f"用户 {self.username} 已退出")

    def update_email(self, new_email: str):
        if "@" not in new_email:
            print("邮箱格式不正确")
            return False
        self.email = new_email
        return True

    def deactivate(self):
        self.is_active = False


继承与重写：

| 概念 | 写法 | 作用 |
| :--- | :--- | :--- |
| 继承 | `class AdminUser(User):` | 子类复用父类属性和方法 |
| 父类初始化 | `super().__init__(...)` | 先把父类已有属性初始化好 |
| 子类特有属性 | `self.permissions = ...` | 补充子类自己的数据 |
| 方法重写 | 子类重新定义同名方法 | 让同一个方法在不同角色中输出不同结果 |

面向对象的三大特性

| 特性 | 解决什么问题 |
| :--- | :--- |
| 封装 | 把数据和操作放在一起，外部不直接碰数据 |
| 继承 | 子类复用父类已有能力，减少重复代码 |
| 多态 | 同一方法名，不同对象表现出不同行为 |


多态的本质：
调用者不需要知道对象具体是什么类型
只需要知道"这个对象有这个方法"
方法的具体行为由对象自己决定

两种多态形式：

| 形式 | 说明 | 示例 |
| :--- | :--- | :--- |
| 基于继承的多态 | 子类重写父类方法，调用父类引用时执行子类版本 | `User` / `AdminUser` / `StudentUser` 的 `get_profile()` |
| 鸭子类型（Duck Typing） | 不需要继承关系，只要方法名相同就能调用 | 任何有 `get_profile()` 方法的对象都能传入 |



| 对比维度 | 基于继承的多态 | 鸭子类型 |
| :--- | :--- | :--- |
| 是否需要继承 | 需要，子类必须继承父类 | 不需要，任何类都行 |
| 类型安全 | 更安全，类型检查有保障 | 更灵活，但运行时可能报错 |
| 适用场景 | 有明确层级关系（管理员是用户） | 只需要共享方法名（打印任何有 `profile` 的对象） |
| Java/C++ 的多态 | 只能基于继承 | Python 特有，更灵活 |

思考题
1.如果不用类，只用字典 + 函数，也能完成用户管理，为什么还要学习 OOP？
 字典+函数适合简单、临时的脚本；而 OOP 适合复杂、长期维护的系统。核心原因有以下几点：

封装与数据完整性：用字典 {'username': '雨', 'created_at': '...'}，任何外部代码都可以随意修改 created_at，甚至漏掉这个字段（就像你之前报错 missing 'created_at'）。而用类，你可以在 __init__ 里强制初始化属性，甚至设置默认值（如 created_at=None），保证数据的安全和完整。

行为与数据绑定：字典是“死”的数据，函数是“游离”的逻辑。用类可以把数据和操作数据的函数（如 get_info()、submit_homework()）封装在一起。你调用 student1.submit_homework() 比写 submit_homework(student1_dict) 更直观。

复用与扩展（继承）：你之前写的 Student 和 Teacher 都继承自 User。如果用字典，你需要为每种角色写一套重复的校验和格式化逻辑。OOP 可以通过继承直接复用父类的代码，只需实现特有部分。

多态与解耦：当系统有几十种用户类型时，OOP 允许调用方统一处理（如你写的 print_all_profiles([Student1, TeacherUser1])），而不需要写一堆 if role == 'student': ... elif role == 'teacher': ...。




2.继承能减少重复代码，但过度继承可能带来什么问题？
过度继承（继承层次过深、过滥）会导致代码变得极度脆弱和难以维护，常见问题包括：

“脆弱的基类”问题（Fragile Base Class）：父类的任何微小改动，都可能引发底层所有子类发生难以预料的 Bug（蝴蝶效应）。

不必要的接口污染：子类会继承父类所有的方法，哪怕有些方法它根本不需要。比如 User 有个 add_course() 方法，如果 Student 继承了 User，学生也会有 add_course()，这在逻辑上是不对的（学生不能添加课程，只能选课）。

层次结构爆炸：如果 User 下面还有 Person、Animal，层级太深，你要找一个方法的实现，需要一层层往上找，代码的可读性会变得极差。

强耦合：子类和父类紧密绑定，难以拆分解耦。在现代编程中，有一条经典原则叫“组合优于继承”（Composition over Inheritance）。比如把“课程”作为一个属性组合到 Teacher 里，而不是让 Teacher 去继承一个 Course 类。



3.多态的好处是"新增类型不需要改调用方代码"，
请用自己的话举一个生活中的多态例子（提示：比如"充电"这个动作，手机、平板、耳机都可以充电，但充电方式不同）。