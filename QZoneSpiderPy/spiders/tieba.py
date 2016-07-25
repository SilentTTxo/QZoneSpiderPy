# -*- coding: utf-8 -*-
import scrapy

from QZoneSpiderPy.items import TieBaItem

class TiebaSpider(scrapy.Spider):
    name = "tieba"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://tieba.baidu.com/f?ie=utf-8&kw=%E6%B9%96%E5%8D%97%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6&fr=search',
    )

    def parse(self, response):
        items = []
        for sel in response.xpath('//ul[@id="thread_list"]/li'):
        	item = TieBaItem()
        	item['userid'] = sel.xpath('//span[@class="frs-author-name-wrap"]/a/text()').extract()
        	item['link'] = sel.xpath('//a[@class="j_th_tit"]/@href').extract()
        	item['title'] = sel.xpath('//a[@class="j_th_tit"]/text()').extract()
        	item['contents'] = sel.xpath('//div[@class="threadlist_abs threadlist_abs_onlyline "]/text()').extract()
        	items.append(item)
        return items