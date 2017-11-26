# coding=utf-8

# http://table.finance.yahoo.com/table.csv?s=000001.sz, 我们通过雅虎网站获取了中国
# 股市某只股票csv数据文件，现在要下载多只股票的csv数据，并将其转换为xml文件
#
# 额外需求：
# 实现一个线程，将转换出的xml文件压缩打包，比如转换线程每生产出100个xml文件，就通知打包线程
# 将它们打包成一个xxx.tgz文件，并删除xml文件，打包完成后，打包线程反过来通知转换线程，转换线程
# 继续转换

# 线程间的事件通知，可以使用标准库中Threading.Event:
# 1. 等待时间一端调用wait，等待事件
# 2. 通知事件一端调用set，通知事件

import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
from StringIO import StringIO
from threading import Event, Thread
from Queue import Queue
import tarfile
import os

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
    def __init__(self, queue, cEvent, tEvent):
        Thread.__init__(self)
        self.queue = queue
        self.cEvent = cEvent
        self.tEvent = tEvent

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
        count = 0
        while True:
            sid, data = self.queue.get()
            print 'Convert', sid
            if sid == -1:
                self.cEvent.set()
                self.tEvent.wait()
                break
            if data:
                fname = str(sid).rjust(6, '0') + '.xml'
                with open(fname, 'wb') as wf:
                    self.csvToXml(data, wf)
                count += 1
                if count == 5:
                    self.cEvent.set()
                    self.tEvent.wait()
                    self.tEvent.clear()
                    count = 0

class TarThread(Thread):
    def __init__(self, cEvent, tEvent):
        Thread.__init__(self)
        self.count = 0
        self.cEvent = cEvent
        self.tEvent = tEvent
        # 设为守护线程
        self.setDaemon(True)

    def tarXML(self):
        self.count += 1
        tfname = '%d.tgz' % self.count
        tf = tarfile.open(tfname, 'w:gz')
        for fname in os.listdir('.'):
            if fname.endswith('.xml'):
                tf.add(fname)
                os.remove(fname)

        tf.close()

        if not tf.members:
            os.remove(tfname)

    def run(self):
        while(True):
            self.cEvent.wait()
            self.tarXML()
            self.cEvent.clear()

            self.tEvent.set()

if __name__ == '__main__':
    q = Queue()
    dThreads = [DownloadThread(i, q) for i in xrange(1, 11)]

    cEvent = Event()
    tEvent = Event()

    cThread = ConvertThread(q, cEvent, tEvent)
    tThread = TarThread(cEvent, tEvent)
    tThread.start()

    for t in dThreads:
        t.start()
    cThread.start()

    for t in dThreads:
        t.join()

    q.put(-1, None)
