# coding=utf-8

# http://table.finance.yahoo.com/table.csv?s=000001.sz, 我们通过雅虎网站获取了中国
# 股市某只股票csv数据文件，现在要下载多只股票的csv数据，并将其转换为xml文件
#
# 由于全局解释器锁的存在，多线程进行CPU密集型操作并不能提高执行效率，我们修改了程序架构：
# 1. 使用多个DownloadThread线程进行下载(I/O操作)
# 2. 使用一个ConvertThread线程进行转换(CPU密集型操作)
# 3. 下载线程把下载数据安全的传递给转换线程

import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
from StringIO import StringIO
from threading import Thread
from Queue import Queue

# 使用标准库中Queue.Queue, 它是一个线程安全的队列，Download线程把下载数据放入
# 队列，Convert线程从队列里面提取数据


# 生产者
class DownloadThread(Thread):
    def __init__(self, sid, queue):
        Thread.__init__(self)
        self.sid = sid
        self.url = 'http://hq.sinajs.cn/list=sh%s'
        self.url %= str(sid).rjust(6, '0')
        self.queue = queue

    def download(self, url):
        response = requests.get(url, timeout=3)
        if response.ok:
            return StringIO(response.content)

    def run(self):
        print 'Download', self.sid
        data = self.download(self.url)
        self.queue.put((self.sid, data))

# 消费者
class ConvertThread(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def csvToXml(self, scsv, fxml):
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

    def run(self):
        while True:
            sid, data = self.queue.get()
            print 'Convert', sid
            if sid == -1:
                break
            if data:
                fname = str(sid).rjust(6, '0') + '.xml'
                with open(fname, 'wb') as wf:
                    self.csvToXml(data, wf)

q = Queue()
dThreads = [DownloadThread(i, q) for i in xrange(1, 11)]
cThread = ConvertThread(q)
for t in dThreads:
    t.start()
cThread.start()

for t in dThreads:
    t.join()

q.put(-1, None)
