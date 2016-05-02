#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy

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
        # link before 2008
        for newsUrl in response.css(u'span.thin12_black a::attr("href")').re('.*'):
            yield scrapy.Request(response.urljoin(newsUrl), callback=self.parse_old_article) 
        # link after 2008
        for newsUrl in response.css(u'a[title="詳全文"]::attr("href")').re('.*'):
            yield scrapy.Request(response.urljoin(newsUrl), callback=self.parse_article) 

    def parse_article(self, response):
        title = response.css('td.thin20_nthu_story_content_title::text').extract()
        content = response.css('p.thin12_nthu_story_content::text').extract()
        source = response.css('span.thin12_nthu_story_content strong::text').extract_first()
        source = source.strip(u'　【】〔〕')
        yield {'title': title, 'content': content, 'source': source}

    def parse_old_article(self, response):
        title = response.css('div.body h3::text').extract()
        content = response.css('div.newstitle p::text').extract()
        source = response.css('div.body h5::text').extract_first()
        source = source.strip(u'　【】〔〕')
        yield {'title': title, 'content': content, 'source': source}
