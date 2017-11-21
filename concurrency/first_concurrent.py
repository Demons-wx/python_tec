# coding=utf-8

# http://table.finance.yahoo.com/table.csv?s=000001.sz, 我们通过雅虎网站获取了中国
# 股市某只股票csv数据文件，现在要下载多只股票的csv数据，并将其转换为xml文件
#
# 如何使用多线程来提高下载处理的效率？


# 使用标准库threading.Thread创建线程，在每一个线程中下载并转换一只股票数据


#######
# 注意：在python中不适合处理CPU密集型的工作，因为在python中有一个GIL(global interpre
# ter lock)，不能实现真正意义上的并发。
#######

import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
from StringIO import StringIO


def download(url):
    response = requests.get(url, timeout=3)
    if response.ok:
        return StringIO(response.content)

def csvToXml(scsv, fxml):
    reader = csv.reader(scsv)
    headers = reader.next()
    headers = map(lambda h: h.replace(' ', ''), headers)

    root = Element('Data')
    for row in reader:
        eRow = Element('Row')
        root.append('Row')
        for tag, text in zip(headers, row):
            e = Element(tag)
            e.text = text
            eRow.append(e)

        et = ElementTree(root)
        et.write(fxml)

def handle(sid):
    print 'Download...(%d)' % sid
#    url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
    url = 'http://www.baidu.com'
    url %= str(sid).rjust(6, '0')
    rf = download(url)
    if rf is None:
        return

    print 'Convert to XML...(%d)' % sid
    fname = str(sid).rjust(6, '0') + '.xml'
    with open(fname, 'wb') as wf:
        csvToXml(rf, wf)

# 多线程，方式1
from threading import Thread

t = Thread(target=handle, args=(1,))
t.start()

print 'main thread'


