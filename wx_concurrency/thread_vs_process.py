# coding=utf-8

# 通过查找某一范围的水仙花数，对比多进程和多线程
# 水仙花数：指一个 n 位数（n≥3 ），它的每个位上的数字的 n 次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）

from threading import Thread
from multiprocessing import Process

def isArmstrong(n):
    a, t = [], n
    while t > 0:
        a.append(t % 10)
        t /= 10

    k = len(a)
    return sum(x ** k for x in a) == n

def findArmstrong(a, b):
    print a, b
    res = [k for k in xrange(a, b) if isArmstrong(k)]
    print '%s - %s: %s' % (a, b, res)

def findByThread(*argslist):
    workers = []
    for args in argslist:
        worker = Thread(target=findArmstrong, args=args)
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()

def findByProcess(*argslist):
    workers = []
    for args in argslist:
        worker = Process(target=findArmstrong, args=args)
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()

if __name__ == '__main__':
    import time
    start = time.time()
#    findByProcess((20000000, 25000000), (25000000, 30000000))
    findByThread((20000000, 25000000), (25000000, 30000000))
    print time.time() - start
