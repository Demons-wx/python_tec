# coding=utf-8

# http://table.finance.yahoo.com/table.csv?s=000001.sz
# 我们可以通过雅虎网站获取中国股市(深市)数据集，它以csv数据格式存储：
#
# 请将平安银行这支股票，在2016年中成交量超过50000000的记录存储到另一个csv文件中
#
# 使用标准库的csv模块，可以使用其中reader和writer完成csv文件读写

from urllib import urlretrieve

urlretrieve('http://hq.sinajs.cn/list=sh601006', 'gosuncn.csv')

import csv

with open('gosuncn.csv', 'rb') as rf:
    reader = csv.reader(rf)
    with open('gosuncn2.csv', 'wb') as wf:
        writer = csv.writer(wf)
        headers = reader.next()
        writer.writerow(headers)
        for row in reader:
            if row[0] < '2016-01-01':
                break
            if int(row[5]) >= 50000000:
                writer.writerow(row)

print 'end'