from bottleneck import src

from src.utils import get_logger,timer

from src.utils import *
#
# @timer()
# def hi(): print("ok")
# hi()
"""
#异常介绍
    概述，在Python中，我们把所有出现的非正常情况统称为异常
常见的异常：
    FileNotFound
    除零错误
异常的默认类型：
    程序会将异常的类型，产生原因，异常出现的位置，打印到控制台上
    并终止程序的执行
"""

# 1.读取了一个不存在的文件
# src_f = open('1.txt','r')   #FileNotFoundError
#
# #2.除零异常：
# print(10//0)  #ZeroDivisionError
# print('执行')

#捕获异常
"""
    概述：
        捕获异常这种方式执行之后，程序会自动往下执行
    # 基本语法
    try:
        "可能发生的错误代码"
    except: 
        "如果出现异常执行的代码"
    else：
        。。。
    finall：
        。。。。
    执行流程：
    1.先执行try中的内容，看有无问题，有问题会立即跳转到except中
    2.如果try中的无问题，程序会跳过except，跳转到后续过程
    
    捕获所有异常（Exception）：
    try：
        print(name)
    except Exception as e: #as e :输出异常信息
        print(e): 
"""

#演示过程
# 1.读取了一个不存在的文件
#
# try:
#     print('hello 1')
#     src_f = open('tests/1.txt','r') # 此处报错后会立即跳转，后续内容不会执行
#     print('hello 2')#FileNotFoundError
# except:
#     print('文件不存在，请教验后重新操作')
#2.除零异常：
# print(10//0)  #ZeroDivisionError
# print('执行')


"""
至此，已经初识了try except的语法，接下来我们来看看他是如何精确捕获异常的

    格式：
    try：
        可能出现异常的代码
    except Exception as e: 
        出现问题后的解决方案
格式解释：
    Exception 所有异常的父类 即：它代表所有的异常
    e       类似于变量名，这里代表的是异常名
    
细节：
还可以写成except(异常1，异常2) as e 这代表了可以捕获多个异常
    
"""


# 1.读取了一个不存在的文件
# src_f = open('1.txt','r')   #FileNotFoundError
#
# #2.除零异常：
# print(10//0)  #ZeroDivisionError
# print('执行')
#
#3.变量未定义
#print(num) #NameError
#
#捕获单个异常
# try:
#     print(name)
#     src_f = open('1.txt','r')
# except NameError as e:
#     #e 就是异常对象，代表着：异常信息，可以直接把他输出到控制台
#     #except后的变量是对异常捕获的限制，即只能捕获到NameError
#     print('程序出现问题')
#     print(e)

#捕获多个异常 只能捕获到自己定义的异常
# try:
#     print(name) #出现问题以后直接跳转，后续出现异常也不会再捕获
#     src_f = open('1.txt','r')
# except (NameError,FileNotFoundError) as e:
#     print(e)


#通用捕获异常方法
# try:
#     print(name) #出现问题以后直接跳转，后续出现异常也不会再捕获
#     src_f = open('1.txt','r')
# except Exception as e:
#     print(e)

#捕获异常的完整格式
"""
捕获异常的完整格式：
    try:
        可能出现问题的代码
    except [Exception as e]: 
        出现问题的解决方案
    else:
        只要try中内容无问题，就会执行这里面的内容
        只要try中有问题，这里就会被跳过
    finally：
        无论try中是否有问题，都会执行该代码，一般用来释放资源

"""

# try:
#     print('try 1')
#     print(10 // 5)
#     print('try 2')
# except Exception as e:
#     print(f'程序出问题了,{e}')
# else:
#     print('else,程序是否执行')
# finally:
#     print('finally,程序是否执行')



#
# print('执行')

src_f=dast_f = None
try:
#案例：拷贝文件，加入异常处理：

    src_f = open('tests/1.txt', 'rb')
    dast_f = open('tests/2.txt', 'wb')

except Exception as e:
    print(e)
else:
    while True:
        data = src_f.read(1024)
        if len(data) <= 0:
            break
        dast_f.write(data)
finally:
    try:
        src_f.close()
    except Exception as e:
        print(e)
    try:
        dast_f.close()
    except Exception as e:
        print(e)
print('_'*50)

#使用with open 的简便写法
try:
    with open('tests/1.txt', 'rb') as src_f, open('tests/2.txt', 'rb') as dast_f :
        while True:
            data = src_f.read(1024)
            if len(data) <= 0:
                break
            dast_f.write(data)
except Exception as e:
    print(e)

#异常的传递：
#异常具有传递性：当函数function1中发生异常，但是没有捕获，异常就会传递到function2，当fun2也没有捕获时，依然会继续传递
#即异常会传递给它的调用者，若一直没有被捕获，就会传给main函数，直至报错
#利用异常传递性的特点，当我们想要保证程序不会因为一场崩溃时，就可以在主函数中设置异常捕获
#由于整个程序中无论哪里发生异常，最后都会传递到主函数中，所以我们可以直接在主函数中对异常进行捕获
