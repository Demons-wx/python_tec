# coding=utf-8

# 某班英语成绩以字典形式存储为：{'Lilei': 79, 'Jim': 88, 'Lucy': 92...}
# 根据成绩高低，计算学生排名

# 1. 使用内置函数sorted
from random import randint

scores = {x : randint(60, 100) for x in 'xyzabc'}
print scores
# 利用zip将字典数据转化为元组
scores_tuple = zip(scores.itervalues(), scores.iterkeys())
# 传递sorted函数的key参数
print sorted(scores_tuple)

# 2.
print sorted(scores.items(), key=lambda x : x[1])