# coding=utf-8

# 实现一个连续浮点数发生器FloatRange(和xrange类似)，根据给定范围(start, end)和
# 进步值(step)产生一些连续浮点数，如迭代FloatRange(3.0, 4.0, 0.2)可产生序列：
# 正向：3.0->3.2->3.4->3.6->3.8->4.0
# 反向：4.0->3.8->3.6->3.4->3.2->3.0

# 列表的反向迭代
# l = [1, 2, 3, 4, 5]
# for x in reversed(l):
#     print x

class FloatRange:
    def __init__(self, start, end, step = 0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

# 正向迭代
for x in FloatRange(1.0, 4.0, 0.5):
    print x

# 反向迭代
for x in reversed(FloatRange(1.0, 4.0, 0.5)):
    print x
