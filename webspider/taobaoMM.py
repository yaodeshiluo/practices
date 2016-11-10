import urllib
import urllib2
import re

class Spider:
    def __init__(self):
        self.baseUrl = 'https://mm.taobao.com/json/request_top_list.htm'

    def getPage(self,pageIndex):
        url = self.baseUrl + '?page=' + str(pageIndex)
        request = urllib2.Request(url)
        respond = urllib2.urlopen(request)
        return respond.read().decode('gbk')
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            contents.append([item[0],item[1],item[2],item[3],item[4]])
        return contents
    def getDetailPage(self,infoUrl):
        respond = urllib2.urlopen(infoUrl)
        return respond.read().decode('gbk')
    def getBrief(self,page):
        pattern = re.compile()


    def saveImg(self,imageUrl,fileName):
        u = urllib.urlopen(imageUrl)
        data = u.read()
        f = open(fileName,'wb')
        f.write(data)
        f.close()

spider = Spider()
page = spider.getPage(1)
print page


import urllib
import urllib2
import re

baseUrl = 'https://mm.taobao.com/json/request_top_list.htm'
url = baseUrl + '?page=' + str(1)
request = urllib2.Request(url)
respond = urllib2.urlopen(request)
pattern = re.compile(
    '<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',
    re.S)
page = respond.read().decode('GBK')
items = re.findall(pattern, page)
items2 = re.search(pattern,page)


print type(respond.read())
page = respond.read().decode('GBK')
print page