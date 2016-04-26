import sys
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.spider import Spider
from scrapy.selector import Selector
from ..items import PeopleItem
from itertools import izip
from collections import defaultdict
import json
import codecs

allnews = defaultdict(tuple)
tmp = []

urls = [line.strip() for line in file("/Users/shanny/Documents/ILS/people/url_2016.txt")]


class PeopleSpider(scrapy.Spider):
    name = "myPeople"
    allowed_domains = ["http://www.nthu.edu.tw/"]  # 5728-5110 p.229
    start_urls = ["http://www.nthu.edu.tw/newsphoto/%s" % line.strip() for line in urls]
    # print start_urls

    def parse(self, response):
        # fileout = open('presidents.txt', 'w')
        # caption = response.selector.xpath('//td[@class="caption"]//text()').extract()
        header = response.selector.xpath('//td[@class="thin20_nthu_story_content_title"]/text()').extract()
        time = response.selector.xpath('//span[@class="thin12_nthu_story_content"]/strong/text()').extract()
        content = response.selector.xpath('//p[@class="thin12_nthu_story_content"]/text()').extract()

        print header[0]
        print time[0]
        for c in content:
            print c
        allnews['header'] = header[0].strip()
        allnews['time'] = time[0].strip()
        # allnews['source'] = content[1].strip()
        # allnews['reporter'] = content[1].strip().split(' ')[2]
        allnews['content'] = [c.strip() for c in content]

        # print json.dumps(allnews, encoding="utf8", ensure_ascii=False)
        with codecs.open("example-out.json", "a", encoding="utf8") as fout:
            json.dump(allnews, fout, ensure_ascii=False, indent=4)
