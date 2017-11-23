# coding=utf-8

# 某软件要求，从网络抓取各个城市气温信息，并依次显示：
# 北京 15~20
# 天津 17~22
# 长春 12~18
#
# 如果一次抓取所有城市天气再显示，显示第一个城市气温时，有很高的延时，并且浪费存储空间，
# 我们期望以`用时访问`的策略，并且能把所有城市气温封装到一个对象里，可用for语句进行迭代，如何解决。

# step1: 实现一个迭代器对象WeatherIterator, next方法每次返回一个城市气温
# step2: 实现一个可迭代对象WeatherIterable, __iter__方法返回一个迭代器对象

import requests

def getWeather(city):
    r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
    data = r.json()['data']['forecast'][0]
    return '%s: %s, %s ' % (city, data['low'], data['high'])

# print getWeather(u'北京')
# print getWeather(u'长春')
# print getWeather(u'深圳')

from collections import Iterable, Iterator

class WeatherIterator(Iterator):

    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s ' % (city, data['low'], data['high'])

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

class WeatherIterable(Iterable):

    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

for x in WeatherIterable([u'北京', u'上海', u'深圳', u'西安', u'哈尔滨']):
    print x