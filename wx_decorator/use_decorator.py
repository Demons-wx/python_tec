# coding=utf-8

# 某些时候我们想为多个函数，统一添加某种功能，比如计时统计，记录日志，缓存运算结果等
#
# 我们不想在每个函数内一一添加完全相同的代码，有什么好的解决方案？
#
# 解决方法：定义装饰器函数，用它来生成一个在原函数基础添加了新功能的函数，替代原函数

# 【题目1】斐波那契数列
# def fibonacci(n):
#     if n <= 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print fibonacci(50)

# 上述写法，会有很多子问题被重复计算，解决方法是：加入一个缓存，当当前数值已被计算过，则直接取缓存中的结果

# 【改写】
# def fibonacci(n, cache=None):
#     if cache is None:
#         cache = {}
#     if n in cache:
#         return cache[n]
#
#     if n <= 1:
#         return 1
#     cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
#     return cache[n]
#
# print fibonacci(50)

# 【使用装饰器模式】
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print fibonacci(50)