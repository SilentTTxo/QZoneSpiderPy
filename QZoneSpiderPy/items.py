# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QzonespiderpyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class DmozItem(scrapy.Item):
	title = scrapy.Field()
	link = scrapy.Field()
	desc = scrapy.Field()
class TieBaItem(scrapy.Item):	
	userid = scrapy.Field()
	title = scrapy.Field()
	contents = scrapy.Field()
	link = scrapy.Field()
	date = scrapy.Field()