# coding=utf-8

# 有某个文本文件，我们想读取其中某范围的内容如100~300行之间的内容，python中文本文件是
# 可迭代对象，我们是否可以使用类似列表切片的方式得到一个100~300行文件内容的生成器？
# f = open('/var/log/dmesg') f[100:300] 可以吗？

# 使用标准库中的itertools.islice，它能返回一个迭代对象切片的生成器

f = open('/Users/wangxuan/Doc/文档/学习文件/tale.txt')

from itertools import islice

# 100~300行
for line in islice(f, 100, 300):
    print line

# 前500行
islice(f, 500)

# 100~最后
islice(f, 100, None)

# islice会消耗迭代过的对象
l = range(20)
t = iter(l)
for x in islice(t, 5, 10):
    print x

print '=' * 20

for x in t:
    print x
