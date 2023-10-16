"""
函数参数学习

Version: 0.1
Author: chengxm
"""

from random import randint

def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total

def add(a= 0,b=0, c=0):
    """三个数相加"""
    return a + b + c


#如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
#摇三个色子
print(roll_dice(3))
print(add())
print(1)
print(add(1,2))
print(add(1, 2, 3))
#传递参数时，可以不按照设定的顺序进行传递
print(add(c=50, a = 100, b = 200))