# -*- coding: utf-8 -*-
import scrapy

from QZoneSpiderPy.items import TieBaItem

class TiebaSpider(scrapy.Spider):
    name = "tieba"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://tieba.baidu.com/f?kw=湖南科技大学&ie=utf-8&pn=0',
    )

    def parse(self, response):
        for sel in response.css('[class=" j_thread_list clearfix"]'):
            if len(sel.css('a.j_th_tit::text').extract()) != 1:
                continue
            item = TieBaItem()
            item['userid'] = sel.css('.frs-author-name-wrap>a::text').extract()
            item['link'] = sel.css('a.j_th_tit::attr(href)').extract()
            item['title'] = sel.css('a.j_th_tit::text').extract()
            item['contents'] = sel.css('div.threadlist_abs::text').extract()
            item['date'] = sel.css('.threadlist_reply_date::text').extract()
            yield item

        for url in response.css('.pagination-item::attr(href)').extract():
            if url[-3:] != "-1":
                yield scrapy.Request(url,callback=self.parse)
            else:
                return