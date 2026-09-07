"""
test - 
Date:2026/9/3
"""
"""
# debug_demo.py
使用步骤：
1.加断点
    哪里不会点哪里
2.启动debug
    右键 =》 Debug as
3.看哪里：
    下左：Frame/MainThread： 可以查看执行到哪里了
    下中：Varizbles:变量，可以查看变量的变化过程
    下右：consle 可以查看程序的执行结果
4.如何进行下一步调试
    F7: 逐过程调试：遇见自己写的函数，会转到函数内部
    F8：逐行调试，遇见自己写的函数，不会转移到内部
    F9：逐段调试，直接跳转到下一个断点，如果是最后一个断点，再次按下F9会一次性执行完后续所有的代码
5.如何结束调试
    场景1：调试完
    场景2：手动关
    场景3：最后一个断点执行完
6.如何删除断点
    场景1：再次点击即可
    场景2：点击break points 移除断点
"""
# def calculate_total(prices, quantities):
#     """计算商品总价（故意藏一个 Bug）。"""
#     total = 0
#     for i in range(len(prices)):
#         total += prices[i] * quantities[i]
#     return total
#
#
# def apply_discount(total, rate):
#     """应用折扣。"""
#     return total * (1 - rate)
#
#
# if __name__ == "__main__":
#     prices = [100, 200, 150, 300]
#     quantities = [2, 1, 3]              # ⚠️ 故意少一项
#     subtotal = calculate_total(prices, quantities)
#     final = apply_discount(subtotal, 0.1)
#     print(f"折后总价: {final}")
#

# c ,d , e = 10,20,30
c = 10
d = 20
e = 15
if c >= d:
    if c >= e:
        max = c
    else:
        max = e
else:
    if d>= e:
        max = d
    else:
        max = e
print(f'最大值为：{max}')


