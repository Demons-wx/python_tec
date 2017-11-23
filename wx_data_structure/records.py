# coding=utf-8

# 很多应用程序都有浏览用户的历史记录的功能，例如：
# 浏览器可以查看最近访问过的网页
# 视频播放器可以查看最近播放过的视频
# shell可以查看用户输入过的命令
#
# 现在我们制作了一个简单地猜数字小游戏，添加历史记录功能，显示用户最近猜过得数字，如何实现？



# 使用容量为n的队列存储历史记录
# 使用标准库collections中的deque，它是一个双端循环队列，程序退出前，可以使用pickle
# 将队列对象存入文件，再次运行程序时将其导入

from random import randint
from collections import deque

N = randint(0, 100)
history = deque([], 5)

def guess(k):
    if k == N:
        print 'right'
        return True

    if k < N:
        print '%s is less than N' % k
    else:
        print '%s is greater than N' % k
    return False

while True:
    line = raw_input("please input a number: ")
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print list(history)


import pickle

pickle.dump(history, open('history', 'w'))
print pickle.load(open('history'))