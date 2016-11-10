import scrapy
from daomubiji.items import DaomubijiItem

class mySpider(scrapy.Spider):
    name = 'daomubiji'
    allowed_domains = ['daomubiji.com'] #no /
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        sel = scrapy.selector.Selector()
        tables = sel.xpath('//table')
        items = []
        for each in tables:
            links = each.xpath('tr/td/a/@href').extract() #not tbody
            contents = each.xpath('tr/td/a/text()').extract() #not tbody
            for i in range(len(links)): #forget range!!!!!!!!!!
                item = DaomubijiItem()
                item['link'] = links[i]
                try:
                    item['book'] = contents[i].split(' ')[0]
                    item['chapter'] = contents[i].split(' ')[1]
                except Exception,e:
                    continue

                try:
                    item['bookname'] = contents[i].split(' ')[2]
                except Exception,e:
                    item['bookname'] = contents[i].split(' ')[1][-3:]
                items.append(item)
        return items
















