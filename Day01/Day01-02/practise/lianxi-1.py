"""
将华氏温度转换成摄氏温度

Version: 01
Author: chengxm
"""
f = float(input('请输入华氏温度：'))

c = (f -32) / 1.8

print('%.1f 华氏温度 = %.1f摄氏温度' % (f, c))

