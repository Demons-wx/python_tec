# coding=utf-8

# 将文件内容写入到硬件设备时，使用系统调用，这类I/O操作的时间很长，为了减少I/O
# 操作的次数，文件通常使用缓冲区(有足够多的数据才进行系统调用)文件的缓冲行为，分为
# 全缓冲，行缓冲，无缓冲

# 如何设置python中文件对象的缓冲行为？

# 全缓冲，open函数的buffering设置大于1的整数n，n为缓冲区大小
# 行缓冲，open函数的buffering设置为1
# 无缓冲，open函数的buffering设置为0

f = open('demo.txt', 'w', buffering=2048)
f.write('acd')