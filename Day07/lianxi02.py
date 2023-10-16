s1 = 'hello ' * 3

print(s1)
s2 = 'world'
s1 += s2
print(s1)
print('ll' in s1)
print('Good' in s1)

str2 = 'abcd123456'
print(str2[2])

#字符串切片，从指定开始索引到指定结束索引 结束索引位置不切片
print(str2[2:5])

#无结束索引就切片至最后一位
print(str2[2:])

#双冒号后数字，代表跨位切片，
print(str2[2::2])
#前置无位置表示从第一位开始计算切片
print(str2[::2])

print(str2[::-1])
print(str2[::-2])
print(str2[-3::-1])
