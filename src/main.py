import os
from math import sqrt



import requests
import numpy









def sum1(a, b):
    return a + b


def gcd(a: int, b: int) -> int:
    """总结：计算两个数的最小公倍数
    Args:
        a：数值1
        b：数值2
    Return：
        求出的最小公约数b
    Raise：
        无
    Examle:
        >>> gcd(10,8)
        2
    """
    # x % y = z ----->y是x，z的最大公约数
    while a % b != 0:
        a, b = b, a % b
    return b


x = int(input("请输入x:"))
y = int(input("请输入y："))
print(sqrt(sum1(x, y)))

from utils.logger import get_logger
log = get_logger(__name__, "logs/app.log")