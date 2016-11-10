# -*- coding:utf-8 -*-
import urllib
import urllib2
import re


def getUrl(pageNum):
    baseUrl = 'http://www.qiushibaike.com/hot/'
    if pageNum == 1:
        return 'http://www.qiushibaike.com/hot/'
    elif isinstance(pageNum,int) and pageNum > 1:
        return 'http://www.qiushibaike.com/hot/page/%s/?s=4896654'% pageNum
    else:
        return

def getPage(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    page = response.read().decode('utf-8')
    return page

pageNum = 5
url = getUrl(pageNum)
page = getPage(url)

def getContents(page):
    pattern = re.compile('<div class="content">(.*?)</div>',re.S)
    items = re.findall(pattern,page)
    contents = []
    for item in items:
        content = '\n'+item.strip()+'\n'
        contents.append(content.encode('utf-8'))
    return contents

contents = getContents(page)

file = open('xiaohua.txt','w+')
floor = 1
contentNum = 0
for content in contents:
    pattern = re.compile('<.*?>')
    forWrite=re.sub(pattern,'',content)
    floorTag = '\n'+ str(floor) + '--------------------------------------------------------------------\n'
    file.write(floorTag)
    file.write(forWrite)
    floor +=1
    contentNum +=1

file.close()
