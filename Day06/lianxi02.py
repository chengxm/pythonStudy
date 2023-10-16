"""
输入M和N计算C(M,N)

Version: 0.1
Author: chengxm
"""

def fac(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result
    
m = int(input('m = '))
n = int(input('n = '))
print(fac(m) // fac(n) // fac(m-n))