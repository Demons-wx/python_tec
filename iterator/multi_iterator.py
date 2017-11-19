# coding=utf-8

# 1. 某班学生期末考试成绩，语文，数学，英语分别存储在3个列表中，同时迭代3个列表，计算
# 每个学生的总分(并行)
# 2. 某年级有4个班，某次考试每班英语成绩分别存储在4个列表中，依次迭代每个列表，统计全学年
# 成绩高于90分人数(串行)

from random import randint

chinese = [randint(60, 100) for _ in xrange(40)]
math = [randint(60, 100) for _ in xrange(40)]
english = [randint(60, 100) for _ in xrange(40)]

total = []

# 并行 使用内置函数zip，它能将多个可迭代对象合并，每次迭代返回一个元组
for c, m, e in zip(chinese, math, english):
    total.append(c + m + e)

print total

# 串行 使用标准库中的itertools.chain，它能将多个可迭代对象连接
from itertools import chain

c1 = [randint(60, 100) for _ in xrange(42)]
c2 = [randint(60, 100) for _ in xrange(40)]
c3 = [randint(60, 100) for _ in xrange(39)]
c4 = [randint(60, 100) for _ in xrange(43)]

count = 0
for s in chain(c1, c2, c3, c4):
    if s > 90:
        count += 1

print count
