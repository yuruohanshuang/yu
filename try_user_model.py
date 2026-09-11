"""
try_user_model - 
Date:2026/9/11
"""
from src.models import User, AdminUser, StudentUser


user = User("zhangsan", "zhangsan@example.com")
admin = AdminUser("admin", "admin@example.com")
student = StudentUser("lisi", "lisi@example.com", "S2026001", "AI应用1班")

user.login()
student.login()
student.submit_homework("Day7-OOP用户模型")
admin.disable_user(user)

print("\n--- 普通用户 ---")
print(user.get_profile())

print("\n--- 管理员 ---")
print(admin.get_profile())

print("\n--- 学员用户 ---")
print(student.get_profile())

print(f"\n当前创建用户数: {User.total_count}")