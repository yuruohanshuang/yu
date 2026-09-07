"""
helper - 
Date:2026/9/3
"""
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