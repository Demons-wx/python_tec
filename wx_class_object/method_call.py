# coding=utf-8

# 某项目中，我们代码使用了三个不同库中的图形类: Circle, Triangle, Rectangle
# 他们都有一个获取图形面积的接口，但接口名字不同，我们可以实现一个统一的获取面积的函数，使用
# 每种方法名进行尝试，调用相应类的接口。

# 方法1：使用内置函数getattr, 通过名字在实例上获取方法对象，然后调用
# 方法2：使用标准库operator下的methodcaller函数调用

from lib1 import Rectangle
from lib2 import Triangle
from lib3 import Circle

def getArea(shape):
    for name in ('area', 'getArea', 'get_area'):
        f = getattr(shape, name, None)
        if f:
            return f()

shape1 = Circle(2)
shape2 = Triangle(3, 4, 5)
shape3 = Rectangle(6 ,4)

shapes = [shape1, shape2, shape3]
print map(getArea, shapes)

