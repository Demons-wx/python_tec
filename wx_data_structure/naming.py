# coding=utf-8

'''
学生信息系统中数据为固定格式：(名字, 年龄, 性别, 邮箱地址)
为了减少存储开销，对每个学生信息用元组表示：
('jim', 16, 'male', 'jim8721@gmail.com')
('LiLei', 17, 'male', 'leili@gmail.com')
('Lucy', 16, 'female', 'lucy123@gmail.com')

访问时，我们使用索引访问，大量索引降低程序可读性，
如何解决这个问题？
'''

student = ('jim', 16, 'male', 'jim8721@gmail.com')

# 方案1：定义类似与其他语言的枚举类型，也就是定义一系列数值常量
NAME, AGE, SEX, EMAIL = xrange(4)
# name
print student[NAME]
# age
print student[AGE]

# 方案2：使用标准库中collections.namedtuple替代内置tuple
from collections import namedtuple

Student = namedtuple('Student', ['NAME', 'AGE', 'SEX', 'EMAIL'])
s = Student('jim', 16, 'male', 'jim8721@gmail.com')
print s

# name
print s.NAME
# sex
print s.SEX

