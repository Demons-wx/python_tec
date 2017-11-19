# coding=utf-8

# 有时候我们希望自定义的类，实例间可以使用 <, <=, >, >=, ==, != 符号进行比较，
# 我们自定义比较的行为，有一个矩形的类，我们希望比较两个矩形的实例时，比较的时它们
# 的面积。

# 比较运算符重载，需要实现以下方法：
# __lt__, __le__, __gt__, __ge__, __eq__, __ne__
# 使用标准库下的functools下的类装饰器total_ordering可以简化此过程

from functools import total_ordering
from abc import ABCMeta, abstractmethod

@total_ordering
class Shape(object):

    @abstractmethod
    def area(self):
        pass

    # 只需要定义两个比较函数，其他的比较通过这两个推理得出
    def __lt__(self, other):
        print 'in __lt__'
        if not isinstance(other, Shape):
            raise TypeError('other is not Shape')
        return self.area() < other.area()

    def __eq__(self, other):
        print 'in __eq__'
        if not isinstance(other, Shape):
            raise TypeError('other is not Shape')
        return self.area() == other.area()

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * 3.14


r1 = Rectangle(5, 3)
c1 = Circle(3)

print r1 > c1
