from lianxi01 import Student

def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('陈平安', 22)
    # 给对象发study消息
    stu1.study('python 程序设计')
    # 给对象发watch_mv消息
    stu1.watch_movie()
    stu2 = Student('王大锤',12)
    stu2.study('思想品德')
    stu2.watch_movie()
    # stu2.__seeAge()  执行会报错 Student object has no attribute '__seeAge'

if __name__ == '__main__':
    main()
    