"""
可变参数的相加函数处理

Version: 0.1
Author: chengxm
"""

def add(*args):
    total = 0
    for _ in args:
        total += _
    return total

print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))