"""
my - 
Date:2026/9/10
"""

__all__ = ['fun1', 'fun2']

#函数 = 模块的功能，相当于工具包中的工具
def get_sum(a,b):
    print('我是my_module1 模块的函数')
    return a+b

def fun1():
    print('我是my_module模块的函数')
    print('----fun1-----')


def fun2():
    print('我是my_module模块的函数')
    print('----fun2-----')

#实际开发中，一般会对模块的功能做测试
#如下的测试代码在调用者中也会被执行，但真实的业务场景，测试代码在调用者中是不能被执行的
#解决方案
#答案：__name__属性即可解决这个事，它在当前模块中打印的结果为__main__，
# 在调用者模块中打印的是模块名

#测试代码

#如果条件成立，说明在当前模块中执行
if __name__ == '__main__':
    print(get_sum(10,20))
    fun1()
    fun2()