# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

class QzonespiderpyPipeline(object):
    def process_item(self, item, spider):
        return item

class tiebaPipeline(object):

    def __init__(self):
        self.file = codecs.open('tieba.json', 'w',encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False) + "\n" #这里如果不加ensure_ascii=False，json编码会出问题
        self.file.write(line)
        return item
