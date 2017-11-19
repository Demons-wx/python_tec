# coding=utf-8

# 在web应用中常用json格式传输数据，例如我们利用baidu语音识别服务做语音识别，
# 将本地音频数据post到百度语音识别服务器，服务器响应结果为json字符串：
#
# 在python中如何读写json数据？
#
#
# 使用标准库中的json模块，其中loads，dumps函数可以完成json数据的读写

import json

l = [1, 2, 'abc', {'name': 'bob', 'age':13}]

# 写json
print json.dumps(l)

# 去除空格
print json.dumps(l, separators=[',', ':'])

# 对键排序
print json.dumps(l, sort_keys=True)

with open('demo.json', 'wb') as f:
    json.dump(l, f)


# 读json
l2 = json.loads('[1, 2, "abc", {"age": 13, "name": "bob"}]')
print l2

print l2[3]