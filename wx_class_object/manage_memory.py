# coding=utf-8

# 在python中，垃圾回收器通过引用计数来回收垃圾对象，但某些环状数据结构，存在对象之间的循环引用，
# 比如树的父节点引用子节点，子节点也同时引用父节点，此时同时del掉引用父子节点，两个对象不能立即
# 回收。
#
# 如何解决此类内存管理问题？

# 使用标准库weakref, 它可以创建一种能访问对象但不增加引用计数的对象

import weakref

class Data(object):
    def __init__(self, value, owner):
        self.owner = weakref.ref(owner)
        self.value = value

    def __str__(self):
        return "%s's data, value is %s" % (self.owner(), self.value)

    def __del__(self):
        print 'in Data.__del__'

class Node(object):
    def __init__(self, value):
        self.data = Data(value, self)

    def __del__(self):
        print 'in Node.__del__'

node = Node(100)
del node
