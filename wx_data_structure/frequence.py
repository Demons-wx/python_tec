# coding=utf-8

# 1. 某随机序列[12, 5, 5, 3, 2, 6, 8, 67, ...]中，找出出现次数最高的3个元素，
# 它们出现次数是多少？
from random import randint

sequence = [randint(0, 20) for _ in xrange(30)]

# 方法1
c = dict.fromkeys(sequence, 0)
for x in sequence:
    c[x] += 1

print sorted(c.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

# 方法2 collections.Counter
from collections import Counter
# c2也是一个字典
c2 = Counter(sequence)
# Counter.most_common(n)获取频度最高的n个元素
print c2.most_common(3)


# 2. 对某英文文章的单词，进行词频统计，找到出现次数最高的10个单词，它们出现次数是多少？
import re

txt = open('/Users/wangxuan/Doc/文档/学习文件/tale.txt').read()
# 用非字母的符号进行分割
c3 = Counter(re.split('\W+', txt))
print c3.most_common(10)