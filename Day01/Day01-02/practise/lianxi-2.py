"""
输入半径计算圆的周长和面积

Version: 01
Author: chengxm
"""

f = float(input("请输入圆的半径 ="))

z = 2 * 3.14 * f

m = 3.14 * (f ** 2)

print('半径为 %.1f 的周长 = %.1f' % (f, z))

print('半径为 %.1f 的面积 = %.1f' % (f, m))
