# coding=utf-8

# 实现一个可迭代对象的类，它能迭代出给定范围内所有素数：
# pn = PrineNumbers(1, 30)
# for k in pn:
#   print k;
# 输出结果：
# 2 3 4 7 11 13 17 19 23 29

class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        if k < 2:
            return False

        for i in xrange(2, k):
            if k % i == 0:
                return False

        return True

    def __iter__(self):
        for k in xrange(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k

for x in PrimeNumbers(0, 1000000):
    print x