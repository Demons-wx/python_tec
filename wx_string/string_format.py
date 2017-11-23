# coding=utf-8

# 某个字典存储了一系列属性值：
# {
#     "lodDist": 100.0,
#     "SmallCull": 0.04,
#     "DistCull": 500.0,
#     "trilinear": 40,
#     "farclip": 477
# }
# 在程序中，我们想以以下工整的格式将其内容输出，如何处理？
# lodDist   :100.0,
# SmallCull :0.04,
# DistCull  :500.0,
# trilinear :40,
# farclip   :477


# 方法1: 使用字符串的str.ljust(), str.rjust(), str.center()进行左右居中对齐
s = 'abc'
print s.ljust(20)
print s.rjust(20)
print s.center(20)
# 方法2: 使用format()方法，传递类似'<20','>20','^20'参数完成同样的任务
print format(s, '<20')
print format(s, '>20')
print format(s, '^20')

d = {
     "lodDist": 100.0,
     "SmallCull": 0.04,
     "DistCull": 500.0,
     "trilinear": 40,
     "farclip": 477
}

w = max(map(len, d.keys()))
for k in d:
    print k.ljust(w), ":", d[k]
