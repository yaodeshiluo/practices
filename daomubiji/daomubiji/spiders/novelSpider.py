#-*-coding:utf8-*-

from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from daomubiji.items import DaomubijiItem
#Pycharm在这里会提示找不到novelspider,这是因为这个爬虫是放在program这个大的文件夹下的
#这属于误报，程序可以正常运行。

class novSpider(CrawlSpider):
    name = "novspider"
    redis_key = 'nvospider:start_urls'
    start_urls = ['http://www.daomubiji.com/']

    def parse(self,response):
        selector = Selector(response)
        table = selector.xpath('//table')
        items = []
        for each in table:
            content = each.xpath('tr/td/a/text()').extract()
            url = each.xpath('tr/td/a/@href').extract()
            for i in range(len(url)):
                item = DaomubijiItem()  #为了防止后一个数据覆盖前一个数据，需要在每个循环里都实例化一个NovelspiderItem
                item['link'] = url[i]
                # try可以用于检测错误，出现错误以后就会运行except里面的内容。
                try:
                    item['book'] = content[i].split(' ')[0]
                    item['chapter'] = content[i].split(' ')[1]
                except Exception,e:
                    continue

                try:
                    item['bookname'] = content[i].split(' ')[2]
                except Exception,e:
                    item['bookname'] = content[i].split(' ')[1][-3:]
                items.append(item)
        return items

