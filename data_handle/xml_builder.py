# coding=utf-8

# 某些时候，我们需要将其他格式数据转换为xml，例如
# 我们要把平安股票csv文件，转换成相应的xml：
# Date,Open,High,Low,Close,Volume,AdjClose
# 2016-06-30,8,69,8.74,8.66,8.70,36220400,8.70
#
#
# 使用标准库中的xml.etree.ElementTree, 构建ElementTree, 使用write方法写入文件

import csv
from xml.etree.ElementTree import ElementTree, Element, tostring

# e = Element('Data')
# print e.tag
#
# e2 = Element('Row')
# e3 = Element('Open')
# e3.text = '8.80'
#
# e2.append(e3)
# e.append(e2)
#
# print tostring(e)
#
# et = ElementTree(e)
# et.write('demo2.xml')

def csvToXml(fname):
    with open(fname, 'rb') as f:
        reader = csv.reader(f)
        headers = reader.next()

        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)

    return ElementTree(root)

et = csvToXml('pingan.csv')
et.write('pingan.xml')
