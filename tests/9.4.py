"""
9.4 - 
Date:2026/9/4
"""
import logging
import sys
from http.cookiejar import debug
from pathlib import Path
from turtledemo.penrose import start

import logger

from ai_template.src.utils.logger import get_logger

projecy_root = Path(__file__).parent.parent

"""1
练习目标： 用 for + if 完成基础筛选。
练习要求：
给定 nums = [3, -1, 7, 0, -4, 9, 2]
用 for 循环 + if 找出所有正数并存入新列表
同时统计负数的个数
验收点：
输出 [3, 7, 9, 2]
负数计数为 2
不使用列表推导式（练习基本循环结构）
"""

# nums = [3,-1,7,0,-4,9,2]
#
# true_num1 = []
# count1 = 0
# true_num = [num for num in nums if num > 0 ]
#
# print(true_num)
#
# for num in nums :
#     if num > 0:
#         true_num1.append(num)
#     elif num < 0:
#         count1 = count1 + 1
# print(f'{true_num1}')
# print(f'{count1}')
logging.basicConfig(
    level=logging.DEBUG,  # ✅ 正确：使用 logging.DEBUG
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# i = 0
#
# logging.info("开始登录验证")
#
# while i < 3:
#     y = False
#     num = input('请输入密码：')
#     logging.info(f'用户第{i+1}次输入')
#     if num == '' :
#         logging.info('输入为空，跳过')
#         print('查询到未输入，此次不计入')
#         continue
#     if num == '123456':
#         y = True
#         print('密码正确')
#         logging.info('登录成功')
#         break
#     print('密码错误')
#     i += 1
#     logging.info(f"密码错误，剩余 {3 - i} 次")
#
# if not y:
#     print('超过尝试机会')
#     logging.info('超过输出机会')
# get_logger("程序结束")

emails = " alice@test.com , BOB@TEST.COM ,  charlie@test.com "
email = emails.strip().split(',')
email1 = [email.strip().lower() for email in email]


# print(email1)
# for str1 in email1:
#     if str1.startswith('alice'):
#         print(str1)
# print('-'*50)
# for idx, val in enumerate(["a", "b", "c"], start=1):
#     print(f"第 {idx} 个 = {val}")
# data = [12, 7, 25, 3, 19, 8, 31]
# datas = [x ** 2 for x in data if x %2 == 0 ]
# print(datas)
# sort_data = sorted(data,reverse=True)
# sort_data1 = sorted(data,reverse=True)[:3]
# print(sort_data1)
#
# for idx,val in enumerate(sort_data,start=1):
#     print(f'第{idx}个数是{val}')
#

def get_stats(nums):
    return min(nums), max(nums), sum(nums)

lo, hi, total = get_stats([3, 1, 4, 1, 5])
num = (1,2,3,4,5,6,7)
a,b,c,d,e,*f = num
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print(f"min={lo}, max={hi}, sum={total}")
print('_'*50)

text = "the quick brown fox jumps over the lazy dog the fox"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)

print('_'*50)


students = [
    ("张三", "北京"), ("李四", "上海"), ("王五", "北京"),
    ("赵六", "广州"), ("钱七", "上海"), ("孙八", "北京"),
]

count = {}
for name,city in students:
    count[city] = count.get(city,0)+1

print(count)


