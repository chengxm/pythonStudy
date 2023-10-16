"""
打印三角形图案

Version: 0.1
Author: chengxm
"""
row = int(input("请输入行数："))

for i in range(row):
    for _ in range(i+1):
        print('*', end='')
    print()