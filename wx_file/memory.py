#  coding=utf-8

# 1. 在访问某些二进制文件时，希望能把文件映射到内存中，可以实现随机访问(framebuffer设备文件)
#
# 2. 某些嵌入式设备，寄存器被编址到内存地址空间，我们可以映射/dev/mem某范围，去访问这些寄存器
#
# 3. 如果多个进程映射同一个文件，还能实现进程通信的目的
#
# 解决方案：使用标准库中mmap模块的mmap()函数，它需要一个打开的文件描述符作为参数


