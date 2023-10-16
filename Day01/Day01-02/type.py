"""
使用type() 检查变量的类型

Version: 0.1
Author: chengxm
"""
a = 100
b = 12.345
c = 1 + 5j
d = 'hello world'
e = True

print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'complex'>
print(type(d)) # <class 'str'>
print(type(e)) # <class 'bool'>

"""
可以使用python中内置的函数对变量类型进行转换

int(): 将一个数值或字符串转换成整数， 可以指定进制
float(): 将一个字符串转换成浮点数
str(): 将指定的对象转换成字符串形式，可以指定编码
chr(): 将证书转换成该编码对应
"""