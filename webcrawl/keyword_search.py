#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import permutations
# from searchengine import search

if __name__ == '__main__':
    keywords = open('keywords160421.txt').read().decode('utf8').split()
    res = set()
    command = 'scrapy crawl keywordSpider -a keyword="{0}"'

    for tokens in permutations(keywords, 3):
        querystr = ' '.join(tokens).encode('utf-8')
        print command.format(querystr)
        # urls = search(querystr)
        # res.update(urls)

    # for url in res:
    #     print url.encode('utf-8')
