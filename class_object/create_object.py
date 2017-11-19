# coding=utf-8

# 某网络游戏中，定义了玩家类Player(id, name, status...)
# 每有一个在线玩家，在服务器程序内则由一个Player的实例，当在线人数很多时，将产生大量实例
#
# 如何降低这些大量实例的内存开销？
#
# 定义类__slots__属性，它是用来声明实例属性名字的列表。(阻止动态属性绑定)

class Player(object):
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


class Player2(object):
    # 声明实例所拥有属性，无法动态绑定属性
    __slots__ = ['uid', 'name', 'stat', 'level']
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


# 创建对象
p1 = Player(1, 'Jim')
p2 = Player2(1, 'Jim')
# 查看对象的属性差别
print set(dir(p1)) - set(dir(p2)) # set(['__dict__', '__weakref__'])
# 这个字典用于动态绑定属性(很占内存)
print p1.__dict__

# 动态绑定
p1.x = 123
print p1.__dict__

# 字典占用内存
import sys
print sys.getsizeof(p1.__dict__)


