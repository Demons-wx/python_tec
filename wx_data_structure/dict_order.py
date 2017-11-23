# coding=utf-8

# 某编程竞赛系统，对参赛选手编程解题进行计时，选手完成题目后，
# 把该选手解题用时记录到字典中，以便赛后按选手名查询成绩，
# 答题用时越短，成绩越优
# {'Lilei': (2,43), 'Hanmeimei': (5,52), 'Jim': (1,39)...}
# 比赛结束后，需按排名顺序依次打印选手成绩，如何实现？

# 使用collections.OnrderedDict替代内置字典Dict
from collections import OrderedDict

d = OrderedDict()
d['Jim'] = (1, 35)
d['Leo'] = (2, 37)
d['Bob'] = (3, 40)

for k in d:
    print k

# 模拟比赛系统
from time import time
from random import randint

records = OrderedDict()
players = list('ABCDEFGH')
start = time()

for i in xrange(8):
    raw_input()
    p = players.pop(randint(0, 7 - i))
    end = time()
    print i + 1, p, end - start,
    records[p] = (i + 1, end - start)

print
print '-' * 20

for k in records:
    print k, records[k]