# coding=utf-8

# 西班牙足球甲级联赛，每轮球员进球统计：
# 第一轮：{'苏亚雷斯': 1, '梅西': 2, '本泽马': 1, 'C罗':3}
# 第二轮：{'苏亚雷斯': 1, '梅西': 2, '本泽马': 1, 'C罗':3}
# 第三轮：{'苏亚雷斯': 1, '梅西': 2, '本泽马': 1, 'C罗':3}
# ...
# 统计出前N轮，每场比赛都有进球的球员

from random import randint, sample

# 随机取样
sample('abcdefg', randint(3, 6))

s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

print s1, s2, s3

# 方法1
res = []

for k in s1:
    if k in s2 and k in s3:
        res.append(k)

print res

# 方法2
# step1: 使用字典的viewkeys()方法，得到一个字典keys的集合
# step2: 使用map函数，得到所有字典的keys的集合
# step3: 使用reduce函数，取所有字典的keys的集合的交集
print reduce(lambda a, b : a & b, map(dict.viewkeys, [s1, s2, s3]))


