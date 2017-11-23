# coding=utf-8

from random import randint

# 生成一个随机数列表
from timeit import timeit

data = [randint(-10, 10) for _ in xrange(10)]
print data

# 过滤掉负数
# 方法1 filter
filter_data = filter(lambda x : x >=0, data)
print filter_data

# 方法2 列表解析
list_parser = [x for x in data if x >= 0]
print list_parser

# 生成一个字典(学号：成绩)
d = {x: randint(60, 100) for x in xrange(1, 21)}
print d

# 字典解析
dict_parser = {k: v for k, v in d.iteritems() if v > 90}
print dict_parser

# 生成一个集合
s = set(data)
set_parser = {x for x in s if x % 3 == 0}
print set_parser