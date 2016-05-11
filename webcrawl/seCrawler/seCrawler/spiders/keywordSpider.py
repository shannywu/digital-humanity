import scrapy
from scrapy.spiders import Spider
from seCrawler.common.searResultPages import searResultPages
from seCrawler.common.searchEngines import SearchEngineResultSelectors
from seCrawler.common.searchEngines import SearchEngines
from scrapy.selector import Selector


class keywordSpider(Spider):
    name = 'keywordSpider'
    allowed_domains = ['bing.com', 'google.com', 'baidu.com']
    start_urls = []
    keyword = None
    searchEngine = None
    selector = None
    maxpage = None

    def __init__(self, keyword, se='bing', maxpage=10):
        self.keyword = keyword.lower()
        self.searchEngine = se.lower()
        self.selector = SearchEngineResultSelectors[self.searchEngine]
        self.start_urls.append(SearchEngines[se].format(keyword, 1))
        self.maxpage = maxpage

    def parse(self, response):
        for url in response.xpath(self.selector).re('^https?://.*'):
            yield {'url': url}

        currentPage = int(response.css('a.sb_pagS::text').extract_first())
        nextUrl = response.css('a.sb_pagN::attr("href")').extract_first()
        if nextUrl and currentPage < self.maxpage:
            nextUrl = response.urljoin(nextUrl)
            yield scrapy.Request(nextUrl, callback=self.parse)
