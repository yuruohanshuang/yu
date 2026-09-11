"""
9.11 - 
Date:2026/9/10
"""

from datetime import datetime

# def is_valid_phone(phone: str) -> bool:
#     return len(phone) == 11 and phone.isdigit()
#
# #类:OOP = 用“对象”把一组相关数据和操作这组数据的方法放在一起。
# class Course:
#     def __init__(self,name,teacher,hours,students = None):
#         self.name = name
#         self.teacher = teacher
#         self.hours = hours
#         self.students = students if students is not None else []
#
#     def add_student(self):
#         if self.name not in self.students:
#             self.students.append(self.name)
#             print('成功添加学生')
#         else:
#             print('学生已存在')
#
#     def remove(self):
#         if self.name in self.students:
#             self.students.remove(self.name)
#             print('成功删除学生')
#         else:
#             print('学生不存在')
#
#     def get_info(self):
#         return {'课程名':self.name,'教师':self.teacher,'学时':self.hours,'学生列表':self.students}
#
# Course1 = Course('Python','张三',120,['张三','李四'])
# print(type(Course1.get_info()))

#
# class User:
#     """系统用户."""
#     platform_name = 'AI学习平台'
#     total_count = 0
#     default_role = "user"
#     def __init__(self, username: str, email: str,phone:str):
#         self.username = username
#         self.email = email
#         self.phone = phone
#         self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.is_logged_in = False
#         User.total_count += 1
#
#     def get_profile(self) -> dict:
#         return {
#             "role": User.default_role,
#             "platform_name": User.platform_name,
#             "username": self.username,
#             "email": self.email,
#             "phone": self.phone,
#             "created_at": self.created_at,
#             "is_logged_in": self.is_logged_in,
#
#         }
#

# user1 = User("zhangsan", "zhangsan@example.com","1233432534")
# user2 = User("lisi", "lisi@example.com","21412353245")
# User.default_role = "member"
# User.platform_name = "AI"
# user3 = User("wangwu", "wangwu@example.com","21412353245")
# print(user1.get_profile())
# print(user2.get_profile())
# print(user3.get_profile())
# print(f"当前用户总数: {User.total_count}")

#
# class User:
#     """把状态修改封装到对象方法中."""
#     total_count = 0
#     def __init__(self, username: str, email: str,phone:str):
#         self.phone = phone
#         self.username = username
#         self.email = email
#         self.is_logged_in = False
#         self.is_active = True
#         User.total_count += 1
#
#     def login(self) -> bool:
#         if not self.is_active:
#             print(f"用户 {self.username} 已被禁用，无法登录")
#             return False
#         self.is_logged_in = True
#         print(f"用户 {self.username} 登录成功")
#         return True
#
#     def logout(self):
#         self.is_logged_in = False
#         print(f"用户 {self.username} 已退出")
#
#     def update_phone(self,new_phone:str):
#         if not is_valid_phone(new_phone):
#             print("手机号格式不正确")
#             return False
#         self.phone = new_phone
#         return True
#
#     def update_email(self, new_email: str):
#         if "@" not in new_email:
#             print("邮箱格式不正确")
#             return False
#         self.email = new_email
#         return True
#
#     def deactivate(self):
#         self.is_active = False
#         self.is_logged_in = False
#
#     def get_profile(self) -> dict:
#         return {
#             "username": self.username,
#             "email": self.email,
#             "phone": self.phone,
#             "is_logged_in": self.is_logged_in,
#             "is_active": self.is_active,
#         }

# user1 = User("zhangsan", "zhangsan@example.com","1233432534")
# user2 = User("lisi", "lisi@example.com","21412353245")
#
# user3 = User("wangwu", "wangwu@example.com","21412353245")
#
# user1.update_phone("12345678901")
# user2.update_phone("1212")
#
# print(user1.get_profile())
# print(user2.get_profile())
# print(user3.get_profile())
# print(f"当前用户总数: {User.total_count}")

# class User:
#     """用户基类."""
#
#     def __init__(self, username: str, email: str):
#         self.username = username
#         self.email = email
#         self.is_active = True
#
#     def get_profile(self) -> dict:
#         return {"username": self.username, "email": self.email, "role": "user"}
#
#
# class AdminUser(User):
#     """管理员用户."""
#
#     def __init__(self, username: str, email: str, permissions: list[str] | None = None):
#         super().__init__(username, email)
#         self.permissions = permissions or ["read", "write", "disable_user"]
#
#     def disable_user(self, user: User):
#         if "disable_user" not in self.permissions:
#             print("权限不足")
#             return False
#         user.is_active = False
#         print(f"管理员 {self.username} 禁用了用户 {user.username}")
#         return True
#
#     def get_profile(self) -> dict:
#         profile = super().get_profile()
#         profile["role"] = "admin"
#         profile["permissions"] = self.permissions
#         return profile
#
# class StudentUser(User):
#     """学员用户."""
#
#     def __init__(self, username: str, email: str, student_id: str, class_name: str):
#         super().__init__(username, email)
#         self.student_id = student_id
#         self.class_name = class_name
#         self.homeworks = []
#
#     def submit_homework(self, title: str):
#         self.homeworks.append(title)
#         print(f"学员 {self.username} 已提交作业: {title}")
#
#     def remove_homework(self,title:str):
#         if title in self.homeworks:
#             self.homeworks.remove(title)
#             print(f"学员{self.username}已删除作业{title}")
#         else:
#             print(f"学员{self.username}中不存在作业{title}")
#
#     def get_profile(self) -> dict:
#         profile = super().get_profile()
#         profile.update({
#             "role": "student",
#             "student_id": self.student_id,
#             "class_name": self.class_name,
#             "homeworks": self.homeworks,
#         })
#         return profile
#
# class TeacherUsers(User):
#     def __init__(self,username: str, email: str,teacher_id: str,courses: str):
#         super().__init__(username,email)
#         self.teacher_id = teacher_id
#         self.courses = courses
#
#     def get_profile(self) -> dict:
#         profile = super().get_profile()
#         profile.update({
#             "role": "teacher",
#             "teacher_id": self.teacher_id,
#             "courses": self.courses,
#         })
#         return profile
#

# StudentUser1 = StudentUser("林","1123@email.com","001","数学")
# StudentUser1.submit_homework('数学1')
# StudentUser1.remove_homework('英语1')
# print(StudentUser1.get_profile())





#关于继承的多态

class User:
    """用户基类."""

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.is_active = True

    def get_profile(self) -> dict:
        return {"username": self.username, "email": self.email, "role": "user"}


class AdminUser(User):
    """管理员用户."""

    def __init__(self, username: str, email: str, permissions: list[str] | None = None):
        super().__init__(username, email)
        self.permissions = permissions or ["read", "write", "disable_user"]

    def get_profile(self) -> dict:
        profile = super().get_profile()
        profile["role"] = "admin"
        profile["permissions"] = self.permissions
        return profile


class StudentUser(User):
    """学员用户."""

    def __init__(self, username: str, email: str, student_id: str, class_name: str):
        super().__init__(username, email)
        self.student_id = student_id
        self.class_name = class_name
        self.homeworks = []

    def get_profile(self) -> dict:
        profile = super().get_profile()
        profile.update({
            "role": "student",
            "student_id": self.student_id,
            "class_name": self.class_name,
        })
        return profile

class TeacherUser(User):
    def __init__(self, username: str, email: str, teacher_id: str, courses: str):
        super().__init__(username, email)
        self.teacher_id = teacher_id
        self.courses = courses

    def get_profile(self) -> dict:
        profile = super().get_profile()
        profile.update({
            "role":"teacher",
            "teacher_id": self.teacher_id,
            "courses": self.courses,
        })
        return profile

class Club:
    def __init__(self,username:str,club_name:str):
        self.username = username
        self.club_name = club_name

    def get_profile(self) -> dict:
        return {"username": self.username, "club_name": self.club_name, "role": "club"}
# ===== 多态的核心演示 =====

def print_profile(obj):
    """接收任意对象，调用 get_profile()。

    调用者不需要知道 obj 是普通用户、管理员还是学员，
    只要知道 obj 有 get_profile() 方法就行。
    方法具体执行哪种行为，由对象自己决定。
    """
    profile = obj.get_profile()
    # 用 .get() 容错：不同对象返回的字典结构可能不同
    name = profile.get("username") or profile.get("name") or "未知"
    role = profile.get("role", "未知")
    print(f"[{name}] 角色为 {role}")
    print(f"  完整资料: {profile}")
    print()


# 创建三种对象
# user = User("zhangsan", "zhangsan@test.com")
# admin = AdminUser("admin", "admin@test.com")
# student = StudentUser("lisi", "lisi@test.com", "S001", "AI一班")
#
# # 同一个函数，传入不同对象，输出不同结果
# print_profile(user)
# print_profile(admin)
# print_profile(student)
#鸭子类型：Python 的多态不强制要求继承关系，只要对象有同名方法就能调用：
class Course:
    """课程类，和 User 没有继承关系."""

    def __init__(self, name: str, teacher: str):
        self.name = name
        self.teacher = teacher

    def get_profile(self) -> dict:
        return {"name": self.name, "teacher": self.teacher, "role": "course"}


# Course 和 User 没有继承关系
# 但它也有 get_profile() 方法
# course = Course("Python 编程", "李老师")
#
# # 同一个 print_profile 函数，照样能处理
# print_profile(course)

TeacherUser1 = TeacherUser('雨','1212@email.com','001','Python')
print_profile(TeacherUser1)
Club1 = Club('林','SEES')
print_profile(Club1)
