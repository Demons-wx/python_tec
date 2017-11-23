# coding=utf-8

# 某文件系统目录下有一系列文件：
# quicksort.c
# graph.py
# heap.java
# intall.sh
# stack.cpp
# ...
# 编写程序给其中所有.sh文件和.py文件加上用户可执行权限

# 使用字符串的str.startswith()和str.endswith()方法，注意：多个匹配时参数使用元组

import os, stat

s = [name for name in os.listdir('.') if name.endswith(('.sh', '.py'))]
for x in s:
    os.chmod(x, os.stat(x).st_mode | stat.S_IXUSR)

