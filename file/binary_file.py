# coding=utf-8

# wav是一种音频文件的格式，音频文件为二进制文件，wav文件由头部信息和音频采样数据构成，
# 前44个字节为头部信息，包括声道数，采样频率，pcm位宽等等，后面是音频采样数据。
#
# 使用python，分析一个wav文件头部信息，处理音频数据

f = open('/Users/wangxuan/Music/QQ音乐/林俊杰 - 可惜没如果.wav', 'rb')

info = f.read(44)

import struct

# 音道数
print struct.unpack('h', info[22:24])

# 采样频率
print struct.unpack('i', info[24:28])

# 编码宽度
print struct.unpack('h', info[34:36])

# 数据
import array

f.seek(0, 2)
print f.tell()

n = (f.tell() - 44) / 2
buf = array.array('h', (0 for _ in xrange(n)))
f.seek(44)
f.readinto(buf)

# 将音频文件的声音变小
for i in xrange(n):
    buf[i] /= 8

f2 = open('demo2.wav', 'wb')
f2.write(info)

buf.tofile(f2)
f2.close()

