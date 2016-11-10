# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomubijiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book = scrapy.Field()
    chapter = scrapy.Field()
    bookname = scrapy.Field()
    link = scrapy.Field()
