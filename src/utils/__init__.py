def gcd(a: int, b: int) -> int:
    """一句话总结 第一行做什么  总结：计算两个数的最小公倍数

    Args:参数列表（带类型与说明）
        a(int)：数值1
        b(int)：数值2

    Return：返回值结
        求出的最小公约数 整数b
    Raise：可能抛出的异常
        无
    Examle:至少一个调用示例
        >>> gcd(10,8)
        2
    """
    # x % y = z ----->y是x，z的最大公约数
    while a % b != 0:
        a, b = b, a % b
    return b
