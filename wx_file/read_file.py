# coding=utf-8

# 某文本文件编码格式已知(如utf-8,gbk,big5)在pyhton2.x和python3.x中分别如何读取该文件？
#
# python2 写入文件前对unicode编码，读入文件后对二进制字符串解码
# python3 opne函数指定t的文本模式，endcoding指定编码格式

# python2
f = open('py2.txt', 'w')
s = u'你好'
f.write(s.encode('gbk'))
f.close()

f = open('py2.txt', 'r')
t = f.read()
print t.decode('gbk')

# python3
f = open('py3.txt', 'wt', encoding='utf8')
f.write('你好，世界！')
f.close()

f = open('py3.txt', 'rt', encoding='utf8')
s = f.read()
print(s)