# coding=utf-8

# 1. 过滤掉用户输入中前后多余的空白字符: '  nick2008@gmail.com   '
# 2. 过滤某windows下编辑文本中的'\r': 'hello world\r\n'
# 3. 去掉文本中的unicode组合符号(音调)


# 方法1: 字符串strip(), lstrip(), rstrip()方法去掉字符串两端字符
s = '   abc   123   '
print s.strip()  # 去掉两端的空字符
print s.lstrip() # 去掉左边的空字符
print s.rstrip() # 去掉右边的空字符

# 方法2: 删除单个固定位置的字符，可以使用切片+拼接的方式
s = 'abc:123'
print s[:3] + s[4:]

# 方法3: 字符串的replace()方法或正则表达式re.sub()删除任意位置字符
s = '\tabc\t123\txyz'
print s.replace('\t', '')

s = '\tabc\t123\txyz\ropq\r'
import re
print re.sub('[\t\r]', '', s)

# 方法4: 字符串translate()方法，可以同时删除多种不同字符 (无效)
u = u'ní häo, chī fàn'
print u
print u.translate({0x0301: None})