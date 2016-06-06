#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from nthu.items import NewsItem

# http://stackoverflow.com/questions/1466000/
# urls = map(str.strip(), open'../news_url.txt'))


class NewsSpider(scrapy.Spider):
    name = 'newsspider'
    start_urls = ['http://www.nthu.edu.tw/newsphoto/']

    def parse(self, response):
        # parse yearly page
        for yearPageUrl in response.css('span.ven11_black a:not(.acckey_mainmenu)::attr("href")').re('.*'):
            yield scrapy.Request(response.urljoin(yearPageUrl), callback=self.parse_news_url) 

    def parse_news_url(self, response):
        for newsUrl in response.css(u'a[title="詳全文"]::attr("href")').re('.*'):
            yield scrapy.Request(response.urljoin(newsUrl), callback=self.parse_article) 

    def parse_article(self, response):
        item = NewsItem()
        item['title'] = response.css('p.thin20_nthu_story_content_title::text').extract()
        item['content'] = response.css('p.thin12_nthu_story_content::text').extract()
        yield item
