class Student(object):
    # __init__ 是一个特殊方法用于创建对象时进行初始化操作
    # 同构这个方法我们可以为学生对象绑定name和age属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    
    # PEP 8要求标识符的名字全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法

    def watch_movie(self):
        self.__seeAge();
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)

    # 以上 study watch_movie 都是对象公开的方法，如果希望属性方法是私有的， 给属性名命名是以两个下划线开头如下

    def __seeName(self):
        print('我的名字是%s' % self.name)

    def __seeAge(self):
        print('我的年龄是%s' % self.age)
        