# coding=utf-8

# python中如何解析xml文档？
#
#
# 使用标准库中的xml.etree.ElementTree，其中的parse函数可以解析xml文档

from xml.etree.ElementTree import parse

f = open('demo.xml')
et = parse(f)

root = et.getroot()
print root
print root.tag

# 子元素
for child in root:
    print child.get('name')

print root.find('country')

for e in root.iterfind('country'):
    print e.get('name')

# 所有子元素
print list(root.iter())
print list(root.iter('rank'))

# 高级用法
# 找到country下的所有子元素
print root.findall('country/*')
# 找到任意层次下的子元素
print root.findall('.//rank')
# ..表示父对象
print root.findall('.//rank/..')
# @ 找到包含某一属性的元素
print root.findall('country[@name]')
# 属性等于特定值的元素
print root.findall('country[@name="Singapore"]')
# 指定位置
print root.findall('country[1]')