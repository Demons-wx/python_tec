# coding=utf-8

# 在某些项目中，我们需要获得文件状态，例如：
# 1. 文件的类型(普通文件，目录，符号链接，设备文件...)
# 2. 文件的访问权限
# 3. 文件的最后的访问、修改、节点状态更新时间
# 4. 普通文件的大小

# 系统调用：标准库中os模块下的三个系统调用stat, fstat, lstat获取文件状态
# 快捷函数：标准库中os.path下的一些函数，使用起来更加简洁

import os

s = os.stat('demo.txt')
print s

# 1.
print s.st_mode

import stat

# 判断是否文件夹
print stat.S_ISDIR(s.st_mode)
# 判断是否普通文件
print stat.S_ISREG(s.st_mode)

# 2.
# 读权限
print s.st_mode & stat.S_IRUSR
# 执行权限
print s.st_mode & stat.S_IXUSR

# 3.
# 最后访问时间
import time

print time.localtime(s.st_atime)

# 4.
# 普通文件的大小
print s.st_size

# 使用os.path

# 是否目录
print os.path.isdir('demo.txt')
# 是否符号链接
print os.path.islink('demo.txt')
# 是否普通文件
print os.path.isfile('demo.txt')
# 时间
print os.path.getatime('demo.txt')
# 普通文件大小
print os.path.getsize('demo.txt')
