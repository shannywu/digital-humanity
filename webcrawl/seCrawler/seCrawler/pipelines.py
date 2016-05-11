# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import logging


class SespiderPipeline(object):
    def __init__(self):
        self.file = open('urls.txt', 'a')
        # self.bloomFilter = rBloomFilter.rBloomFilter(100000, 0.01, 'bing')

    def process_item(self, item, spider):
        self.file.write(item['url'].encode('utf-8')+'\n')
        return item
