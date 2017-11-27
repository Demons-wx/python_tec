# coding=utf-8

# 由于python中全局解释器锁(GIL)的存在，在任意时刻只允许一个线程在解释器中运行，
# 因此python的多线程不适合处理cpu密集型的任务。
#
# 想要处理cpu密集型的任务，可以使用多进程模型。

# 使用标准库中multiprocessing.Process，它可以启动子进程执行任务操作接口，进程间通信，
# 进程间同步等都与Threading.Thread类似

from multiprocessing import Process

def f(s):
    print s

p = Process(target=f, args=('hello',))
p.start()

# 多个进程之间的虚拟地址空间是独立的
x = 1
def f():
    global x
    x = 5

p = Process(target=f)
p.start()

print x

# 进程之间如何通信
from multiprocessing import Queue, Pipe

q = Queue()

def f(q):
    print 'start'
    print q.get()
    print 'end'

Process(target=f, args=(q,)).start()
q.put(100)

# 对端读写
c1, c2 = Pipe()
c1.send('abc')
print c2.recv()
c2.send('xyz')
print c1.recv()

def f(c):
    c.send(c.recv() * 2)

c1, c2 = Pipe()
Process(target=f, args=(c2,)).start()
c1.send(55)
print c1.recv()

