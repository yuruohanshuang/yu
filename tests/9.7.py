"""
9.7 - 
Date:2026/9/7
"""
from numpy.ma.core import count
import os
import sys
import math


def circle_info(r:int) :
    """ 计算圆的周长和面积
    Args：r 圆的半径

    Return:圆的周长和面积

    Example：
#        >>> circle_info(3):
    (周长：       面积：)

    """
    l = 2 * 3.14 * r
    s = 3.14 * (r**2)
    return l,s
    print(f'周长：{l}，面积：{s}')

def send_emails(to:str,subject:str="无主题",*,body:str):
    print(f"发送给{to},主题:{subject},内容={body}")


def num_max(nums):
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return max
def calc_ststs(*args) ->dict:
    if not args:
        return {"count": 0, "sum": 0, "avg": 0, "max": None, "min": None}
    count1 = len(args)
    sum1 = math.fsum(args)
    avg = sum1/count1
    max1 = num_max(args)
    min1 = min(args)
    return {"count":{count1}, "sum": {sum1}, "avg": {avg}, "max":{max1}, "min": {min1}}

def make_multiplier(factor):

    def multiplier(x):
        return x * factor
    return multiplier

def make_counter(start: int = 0):
    """创建独立的计数器闭包."""
    count = start

    def step(delta: int = 1) -> int:
        nonlocal count
        count += delta
        return count

    return step
def is_palindrome(s:str) -> bool:
    """判断字符串是否是回文，忽略大小写和非字母数字字符"""
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned==cleaned[::-1]
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                     # False
print(is_palindrome("12321"))

# c1 = make_counter()
# c2 = make_counter(100)
# print(c1())     # 1
# print(c1())     # 2
# print(c2(5))    # 105
# print(c2(5))    # 110   c1 与 c2 互不影响
#
# print('-'*50)
# double = make_multiplier(2)
# triple = make_multiplier(3)
# a = double(5)
# b = triple(5)
# print(f'2:{a},3:{b}')
#
# send_emails(to='lin',body='yu')
# send_emails(to='lin',subject='01',body='yu')
# send_emails('lin','01',body='yu')
#
# l1,s1=circle_info(3)
# print(f'周长：{l1}，面积：{s1}')

# for num in range(1,1000):
#     num1 =  num % 10
#     num2 = num // 10 % 10
#     num3 = num // 100
#     if num1 ** 3 + num2 ** 3 + num3 ** 3 == num:
#         print(num)
# string1 = '是的更符合开始打不开机还不是的方式不对房间号根本就是电饭煲干哈顺丰'
#
# count = {}
#
# for i in string1:
#     if i not in count:
#         count[i] = 0
#     count[i] += 1
# count_keys = sorted(count,key=count.get,reverse=True)
# print(count)
# for key in count_keys[:5]:
#     print(f'{key}:{count[key]:>3d}次')
# nums = [1, 2, 3, 4, 5]

# ❌ 报错：sum(*nums) 等价于 sum(1, 2, 3, 4, 5)，
#         但 sum 只接受一个可迭代对象，不接受多个位置参数
# print(sum(*nums))

# ✅ 正确：定义 calc_sum 用 *args 收集，调用时用 *nums 解包
def calc_sum(*i):
    print(i)          # (1, 2, 3, 4, 5) ← 收集成 tuple
    return sum(i)
# print(calc_sum(*nums))  # 等价于 calc_sum(1, 2, 3, 4, 5) → 15

# # ✅ 字典解包：** 把 dict 拆成关键字参数
# params = {"to": "a@b.com", "body": "hi"}
# send_emails(**params)    # 等价于 send_email(to="a@b.com", body="hi")

# print(calc_ststs())
# print(calc_ststs(*[10,20,30]))
# nums = [1, 2, 3, 4, 5]
#
# print('_'*50)
#
# # map：对每个元素应用函数
# squared = list(map(lambda x: x ** 2, nums))
# print(squared)   # [1, 4, 9, 16, 25]
#
# # 等价于列表推导式
# squared = [x ** 2 for x in nums]
#
# # filter：按条件过滤
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)     # [2, 4]
#
# # 等价于列表推导式
# evens = [x for x in nums if x % 2 == 0]
#
# # sorted：按自定义规则排序
# students = [("张三", 85), ("李四", 92), ("王五", 78)]
# by_score = sorted(students, key=lambda s: s[1], reverse=True)
# print(by_score)   # [('李四', 92), ('张三', 85), ('王五', 78)]

students = [
    ("张三", 85, "北京"),
    ("李四", 92, "上海"),
    ("王五", 78, "北京"),
    ("赵六", 88, "广州"),
]
by_sorted = sorted(students,key=lambda s:s[1],reverse=True)
print(by_sorted)
fil_name = list( filter(lambda s: s[2] == '北京',students))
print(fil_name)
m_name = list(map(lambda s:s[0],students))
print(m_name)