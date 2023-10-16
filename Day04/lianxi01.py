"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: chengxm
"""

from math import sqrt

value = int(input("请输入正整数："))
end = int(sqrt(value))
is_prime = True
for x in range(2, end + 1):
    if value % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print("%d是素数" % value)
else: 
     print("%d不是素数" % value)
