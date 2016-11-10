
from lxml import etree
import requests

response = requests.get('https://movie.douban.com/top250')
# def parse(response):
sel = etree.HTML(response.content)
table = sel.xpath('//div[@class="info"]')
each = table[1]

titlelist = each.xpath('div[@class="hd"]/a/span/text()')
title = ''
for i in titlelist:  # not each!!!!!!!!!!
    title += i

infolist = each.xpath('div[@class="bd"]/p[@class=""]/text()') #
print infolist
s=''
for i in infolist:
    print i
    s += i
print s
starlist = each.xpath('div[@class="bd"]/div/span[@class="rating_num"]/text()')
message = each.xpath('div[@class="bd"]/p[@class="quote"]/span/text()')
if message:
    message = message[0]
else:
    message = ''
item['title'] = title
item['info'] = ';'.join(infolist)
item['star'] = starlist[0]
item['message'] = message
yield item
nextlink = sel.xpath('//span[2class="next"]/link/@href').extract()
if nextlink:
    nextlink = nextlink[0]
print nextlink
yield request(self.url + nextlink, callback=self.parse)