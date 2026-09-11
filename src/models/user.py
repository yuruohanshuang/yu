"""
user - 
Date:2026/9/11
"""
import time
from datetime import datetime


class User:
    platform_name = "学习平台"
    total_count = 0
    def __init__(self,username: str,email: str):
        self.username = username
        self.email = email
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.is_logged_in = False
        self.is_active = False
        User.total_count += 1

    def login(self) -> bool:
        if not self.is_active :
            print(f'用户{self.username}已被禁用,无法登录')
            return False
        self.is_logged_in = True
        print(f'用户{self.username}登录成功')
        return True

    def logout(self) -> bool:
        self.is_logged_in =False
        print(f'用户{self.username}已退出')

    def update_email(self,new_email: str):
        if '@' not in new_email:
            print("邮箱格式不正确")
            return False
        self.email = new_email
        return True
    def get_profile(self):
        return {
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at,
            "is_logged_in": self.is_logged_in,
            "is_active": self.is_active
        }

class AdminUser(User):
    def __init__(self,username: str,email: str,permissions: list[str] | None = None):
        super().__init__(username, email)
        self.permissions = permissions or ["read","write","disable_user"]

    def disable_user(self,user: User):
        if "disable_user" not in self.permissions:
            print("你没有相关的权限")
            return False
        user.is_active = False
        print(f'管理员{self.username}禁用了用户{user.username}')
        return True

    def get_profile(self):
        profile = super().get_profile()
        profile["role"] = "admin"
        profile["permissions"] = self.permissions
        return profile


class StudentUser(User):
    def __init__(self,username,email,student_id,class_name):
        super().__init__(username,email)
        self.student_id = student_id
        self.class_name = class_name
        self.homeworks = []

    def submit_homework(self,homework):
        self.homeworks.append(homework)
        print(f"学员{self.username}已提交了作业{homework}")

    def remove_homework(self, homework: str):
        if homework in self.homeworks:
            self.homeworks.remove(homework)
            print(f"学员{self.username}已删除了作业{homework}")
        else:
            print(f"学员{self.username}没有提交过作业{homework}")

    def get_profile(self) -> dict:
        profile = super().get_profile()
        profile.update({
            "role": "student",
            "student_id": self.student_id,
            "class_name": self.class_name,
            "homeworks": self.homeworks,
        })
        return profile

class Course:
    def __init__(self, name: str, teacher: str,time: str):
        self.name = name
        self.teacher =teacher
        self.time = time


    def get_info(self):
        return {
            "name": self.name,
            "teacher": self.teacher,
            "time": self.time
        }
class Book:
    def __init__(self, bookname: str, author: str):
        self.bookname = bookname
        self.author = author
        self.is_borrow = False

    def borrow_book(self):
        if self.is_borrow:
            print("这本书已经借出去了")
            return False
        self.is_borrow = True
        return True

    def return_book(self):
        if not self.is_borrow:
            print("这本书没有借出去")
            return False
        self.is_borrow = False
        return True

class TeacherUser(User):
    def __init__(self, username: str, email: str,teacher_id: str):
        super().__init__(username, email)
        self.teacher_id = teacher_id
        self.teacher_course = []

    def add_course(self, course: str):
        self.teacher_course.append(course)
        print(f"教师{self.username}添加了课程{course}")

    def get_profile(self):
        profile = super().get_profile()
        profile["role"] = "teacher"
        profile["teacher_id"] = self.teacher_id
        profile["teacher_course"] = self.teacher_course
        return profile


def print_all_profiles(users: list[User]):
    for user in users:
        profile = user.get_profile()
        name = profile.get("username") or profile.get("name") or "未知"
        role = profile.get("role", "未知")
        print(f"用户名：{name}，角色：{role}")
        print(f'详细资料: {profile}')
        print()



if __name__ == '__main__':
    Students1 = StudentUser('雨','1213@email.com',f'{time.ctime()}', '001')
    Students1.submit_homework('数学作业')
    TeacherUser1 = TeacherUser('林','543535@email.com','002')
    TeacherUser1.add_course('数学')

    print_all_profiles([Students1, TeacherUser1])
