# coding=utf-8

# 在某项目中，我们实现了一些类，并希望能像静态类型语言那样对它们的实例属性做类型检查
# p = Person()
# p.name = 'Bob' 必须是str
# p.age = 18 必须是int
# p.height = 1.83 必须是float
#
# 要求：
# 1. 可以对实例变量名指定类型
# 2. 赋予不正确类型时抛出异常

# 使用描述符来实现需要类型检查的属性：
# 分别实现__get__, __set__, __delete__方法，在__set__内使用isinstance函数做类型检查

class Attr(object):
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError('expected an %s' % self.type_)
        instance.__dict__[self.name] = value

    def __del__(self, instance):
        del instance.__dict__[self.name]


class Person(object):
    name = Attr('name', str)
    age = Attr('age', int)
    height = Attr('height', float)

p = Person()
p.name = 'Bob'
print p.name

p.age = '17'
