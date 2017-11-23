# coding=utf-8

# 我们要把某个字符串依据分隔符号拆分不同的字段，该字符串包含多种不同的分隔符，例如：
# s = 'ab;cd|efg|hi,kl|mn\topq;rst,uvw\txyz'
#
# 其中 , ; | \t 都是分隔符号，如何处理？


s = 'ab;cd|efg|hi,kl|mn\topq;rst,uvw\txyz'
# 方法一：连续使用str.split()方法，每次处理一种分隔符号
def mySplit(s, ds):
    res = [s]

    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)), res)
        res = t

    return [x for x in res if x]

print mySplit(s, ';,|\t')


# 方法二：使用正则表达式的re.split()方法，一次性拆分字符串 (推荐)
import re
print re.split(r'[,;\t|]+', s)
