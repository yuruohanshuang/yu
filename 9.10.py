"""
9.10 - 
Date:2026/9/10
"""
import functools
import time
import logging
from threading import Lock
# #异常的传递性：
# 当函数1中出现异常没有被捕获时，就会被传递给调用了函数1的函数2，即异常会传递给调用它的函数
# 根据该性质，我们可以在主函数中设置捕获，这样的话不论函数哪个部分出现异常，我们都可以进行捕获

def fun01():
    print('------fun01-----start')
    print(10//0)
    print('-----fun01 end------')

def fun02():
    print('------fun02 start -----')
    fun01()
    print('------fun02 end------')

def fun03():
    print('--------fun 03 start-----------')
    fun02()
    print('-----fun 03 end-----------')

#模块的导入
"""
模块介绍：
    概述：
        模块指的是module，在Python中，一个.py文件=1个模块
        可以把模块理解为工具包
        工具包中有很多的工具，其实就是：每个.py文件都有很多的函数，这些函数都有不同的功能
    
    学模块就是记忆一些.py文件
    例如随机数用random，日期用time，文件路径相关使用os模块。。。
    
    模块的导入方式：
    方式1：import 模块名·                         后续通过模块名.函数名（）的方式调用   模块下所有函数均可使用
    方式2：import 模块名 as 别名                   后续通过：别名.函数名的但是来调用    模块下所有函数均可使用
    方式3：from 模块名 import 函数名               后续通过：函数名（）的方式调用       只能使用该模块下导入的函数
    方式4：from 模块名 import 函数名 as 别名        后续通过：别名（）的方式直接调用     只能使用该模块下导入的函数
    方式5：from 模块名 import *                   后续通过：函数名（）的方式直接使用   模块下所有函数均可使用

"""
#演示导入模块的几种方式的用法
import random #random工具包

#测试用例：time模块下的sleep（），time（）函数

#演示1 方式1：import 模块名·                         后续通过模块名.函数名（）的方式调用   模块下所有函数均可使用
# import time
#
#
# print('---start---')
# time.sleep(2) #sleep工具  #让程序休，休眠2秒
# print(time.localtime()) #获取系统的本地时间
# print(time.time())  #从时间原点（1970年1月1日：00:00:00~至今的时间）的秒值，
# print('---end---')



#演示2 方式2：import 模块名 as 别名                   后续通过：别名.函数名的但是来调用    模块下所有函数均可使用
# import time as t


# print('---start---')
# t.sleep(2) #sleep工具  #让程序休，休眠2秒
# print(t.localtime()) #获取系统的本地时间
# print(t.time())  #从时间原点（1970年1月1日：00:00:00~至今的时间）的秒值，
# print('---end---')

#演示3 方式3：from 模块名 import 函数名               后续通过：函数名（）的方式调用       只能使用该模块下导入的函数
# from time import sleep,localtime
#
# print('---start---')
# sleep(2) #sleep工具  #让程序休，休眠2秒
# print(localtime()) #获取系统的本地时间
# #print(time.time())  #报错，因为没有导入time函数
# print('---end---')
#演示4 方式4：from 模块名 import 函数名 as 别名        后续通过：别名（）的方式直接调用     只能使用该模块下导入的函数
# from time import sleep,localtime as lt
#
# print('---start---')
# sleep(2) #sleep工具  #让程序休，休眠2秒
# print(lt()) #获取系统的本地时间,用别名来引用
# #print(time.time())  #报错，因为没有导入time函数
# print('---end---')

#演示5 方式5：from 模块名 import *                   后续通过：函数名（）的方式直接使用   模块下所有函数均可使用
# from time import *
# print('---start---')
# sleep(2) #sleep工具  #让程序休，休眠2秒
# print(localtime()) #获取系统的本地时间,用别名来引用
# print(time())  #从时间原点（1970年1月1日：00:00:00~至今的时间）的秒值，
# print('---end---')


"""
案例：演示如何调用自定义模块：


细节：
    1. .py文件就可以看作是一个模块，所以文件名=模块名，所以文件名也要符合标识符的命名规范
    2. __name__属性：当前模块中打印的结果是__main__，在调用者中打印的结果是：调用者的模块名
    3. 如果导入的多个模块中，有同名函数，默认会使用最后导入的那个，因为在导入时，后导入的会覆盖新导入的
    4.__all__属性只针对于from 模块名 import * 这种写法有效，他只会导入__all__记录的内容
"""
#需求：自定义my_module1模块，然后自定义其中一些函数，再调用这些函数
#
# import tests.my_module1 as m1
# import tests.my_module2 as m2

# #错误示范
# from tests.my_module1 import fun1
# from tests.my_module2 import fun1
#
# fun1()
# print(m1.get_sum(10,20))
# m1.fun1()
# m1.fun2()

#    4.__all__属性只针对于from 模块名 import * 这种写法有效，他只会导入__all__记录的内容
from tests.my_module1 import *

# print(get_sum(10,20)) #get_sum报错,因为all属性中没有调用它
# fun1()
# fun2()

"""

# 导包：
包：
    概述：
    文件夹=一堆的.py文件（模块）：本质也是一个模块
    
    背景：
        当我们的模块（.py文件）越来越多的时候，就要分包来进行管理
    
    导包的两种方式：
        1.import 包名.模块名 
            必须通过包名.模块名.函数名（）的方式调用
        2.from 包名 import 模块名 
            必须通过模块名.函数名（）的方式调用
        __all__属性：写在__init__.py 初始化文件中，from包名 import *的时候
        只会导入__all__属性中记录的模块名    
"""
#演示 方式1：import 包名.模块名
#import my_package.my_module1
#包名    模块   函数名
# my_package.my_module1.fun1()
# my_package.my_module1.fun2()
#
#演示 方式2：from 包名 import 模块名
# from my_package import my_module1
# my_module1.fun1()
# my_module1.fun2()

from my_package import * #回去初始化文件__init__.py中，只加载all属性的信息

# my_module1.fun1()




@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(100))
# print(fibonacci.cache_info())

#
#
# if __name__ == '__main__':
#     # try:
#     #     fun03()
#     # except:
#     #     print('除数不能为0')

#装饰器，迭代器，生成器
#定义一个装饰器函数
def outer(func):
    def inner(*args,**kwargs):
        #在func前写的会在执行原函数前触发
        print('准备开始')
        #func(*args,**kwargs)
        value = func(*args,**kwargs)
        print('执行结束')
        print('_'*50)
        #在func后写的会在执行原函数后触发
        return value
    return inner



@outer   #send_wechat = outer(send_wechat) 会立即执行outer
def send_wechat(body):
    print("发送微信",body)
    return 100
@outer
def send_email(to,body):
    print('邮件',to,body)
    return 200
@outer
def send_sms(to,body,*,info):
    print('短信',to,body,info)
    return 300

# if __name__ == '__main__':
#     send_wechat("你好")
#     src = send_wechat('你好')
#     send_sms('yu',"你好",info='byebye')
#     send_email('yu',"你好")
#     print(src)
#

#迭代器,生成器

#迭代器:
# 一种可以被逐个访问的对象,遵循迭代协议,即必须实现
# __iter__()返回迭代器对象本身 和__next__()方法每次调用返回下一个元素,直到跑出StopIteration异常
#迭代器: 使用__iter__来生成迭代器,使用__next__()方法,每次仅返回一个元素
numbers = [10,20,30]

iterator = iter(numbers)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# try:
#     print(next(iterator))
# except:
#     print('没有更多元素')

#生成器:一种特殊的生成器,使用关键字yield逐步生成元素,而不是一次性返回所有数据,生成器比普通迭代器更节约内存

def my_generator():
    yield 1
    yield 2
    yield 3
gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# try:
#     print(next(gen))
# except:
#     print('没有更多元素')

def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b,a+b
# for num in fibonacci(10):
#     print(num)

def infinite_counter():
    num =1
    while True:
        yield num
        num += 1
counter = infinite_counter()
# for _ in range(5):
#     print(next(counter))

#生成器可用于逐行读取大文件,节省内存
def read_large_file(file_path):
    with open(file_path,"r") as file:
        for line in file:
            yield line.strip()
# for line in read_large_file("D:/sucai/1.txt"):
#     print(line)

def chunked(iterable,size):
    if size <= 0:
        raise ValueError("size必须大于0")

    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk
        chunk = []
nums = [1,2,3,4,5,6,7,8,9,10]
for i in chunked(nums,3):
    print(i)

logger = logging.getLogger(__name__)

def rate_limit(per_seconds = 1):
    def decorator(func):
        last_called = 0.0
        lock = Lock()

        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            nonlocal last_called
            with lock:
                current_time = time.monotonic()

                if current_time - last_called <per_seconds:
                    logger.error(f'调用频率过高:{func.__name__}被限流')
                    raise RuntimeError(f'调用{func.__name__}过于频繁,请等待{per_seconds}秒')
                last_called = current_time
            return func(*args,**kwargs)
        return wrapper
    return decorator

# ============ 测试代码 ============
# 配置日志级别方便查看 ERROR 输出
logging.basicConfig(level=logging.ERROR)

@rate_limit(per_seconds=1)
def do_something():
    print("执行业务逻辑...")

do_something() # 第一次，正常输出
time.sleep(0.5)
try:
    do_something() # 第二次，间隔太短，触发限流
except RuntimeError as e:
    print(f"捕获到异常: {e}")
