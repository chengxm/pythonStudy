"""
百分制成绩转换成等级制成绩

Version: 0.1
Author: chengxm
"""

value = float(input("请输入成绩："))

if value >= 90:
    print('%f分以上 = A' % (value))
elif value >= 80:
    print('%f分以上 = B' % (value))
elif value >= 70:
    print('%f分以上 = C' % (value))
elif value >= 60 :
    print('%f分以上 = D' % (value))
else:
    print('%f分以上 = E' % (value))