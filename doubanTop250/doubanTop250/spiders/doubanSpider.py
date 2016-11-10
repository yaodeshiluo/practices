# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request #not request
from scrapy.selector import Selector
from doubanTop250.items import Doubantop250Item #虽然画红线但没错

class doubanSpider(CrawlSpider):
    name = 'douban'
    redis_key = 'douban:start_urls' #urls not url
    start_urls = ['https://movie.douban.com/top250']

    url = 'https://movie.douban.com/top250'
    def parse(self, response):
        sel = Selector(response)
        table = sel.xpath('//div[@class="info"]')
        for each in table:
            item = Doubantop250Item()
            titlelist = each.xpath('div[@class="hd"]/a/span/text()').extract()
            title = ''
            for i in titlelist: #not each!!!!!!!!!!
                title += i

            infolist = each.xpath('div[@class="bd"]/p/text()').extract() #p[1]? 四个str的list？？？？
            starlist = each.xpath('div[@class="bd"]/div/span[@class="rating_num"]/text()').extract()
            message = each.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            if message:
                message = message[0]
            else:
                message = ''
            item['title'] = title
            item['info'] = ';'.join(infolist)
            item['star'] = starlist[0]
            item['message'] = message
            yield item
        nextlink = sel.xpath('//span[@class="next"]/link/@href').extract()
        if nextlink:
            nextlink = nextlink[0]
            print nextlink
            yield Request(self.url + nextlink, callback = self.parse) #大写的Request!!!!!









