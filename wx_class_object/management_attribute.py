# coding=utf-8

# 在面向对象编程中，我们把方法(函数)看作对象的接口，直接访问对象的属性可能是不安全的
# 或设计上不够灵活，但是使用调用方法在形式上不如访问属性简洁。
#
# 能否在形式上是属性访问，但实际上调用方法？
#

# 使用property函数为类创建可管理属性，fget/fset/fdel对应相应属性访问。

from math import pi

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, value):
        if not isinstance(value, (int, long, float)):
            raise ValueError('wrong type')
        self.radius = float(value)

    def getArea(self):
        return self.radius * 2 * pi

    R = property(getRadius, setRadius)

c = Circle(3.2)
print c.R

c.R = 5.9
print c.R

c.R = 'abc'

