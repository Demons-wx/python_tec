# coding=utf-8

# 某项目中，我们从传感器采集数据，每收集到1g数据后，做数据分析，最终只保存分析结果
# 这样很大的临时数据如果常驻内存，将消耗很大内存资源，我们可以使用临时文件存储这些
# 临时数据(外部存储)
#
# 临时文件不用命名，且关闭后会自动被删除
#
# 使用标准库中tempfile下的TemporaryFile, NamedTemporaryFile

from tempfile import TemporaryFile, NamedTemporaryFile

# 由TemporaryFile创建的文件在文件系统中是找不到的，只能由对象f来访问
f = TemporaryFile()
f.write('apple' * 100000)

f.seek(0)

print f.read(100)

# NamedTemporaryFile可在文件系统中访问
ntf = NamedTemporaryFile()
print ntf.name