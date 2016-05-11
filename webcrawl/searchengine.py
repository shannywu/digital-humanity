import sys
import urlparse
from bs4 import BeautifulSoup
from selenium import webdriver
from operator import itemgetter

search_engine = {'Google': 'https://www.google.com.tw/search?q={0}&lr=lang_zh-TW&cr=countryTW',
                 'Bing': 'http://www.bing.com/search?q={0}&rf=1'}

driver = webdriver.Firefox()


def search(query, MAXPAGE=10):
    res = []
    querystr = unicode(query).encode('utf-8')
    queryurl = search_engine['Bing'].format(querystr)
    page = 0

    while page < MAXPAGE:
        driver.get(queryurl)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # google
        # TODO: When request too much in the same time, OCR is needed
        # results = soup.select('#res #search #ires #rso .srg .g .rc .r a')
        # res += map(itemgetter('href'), results)
        # nextPageEle = soup.select('td.navend a')

        # bing
        results = soup.select('ol#b_results .b_algo h2 a')
        res += map(itemgetter('href'), results)
        nextPageEle = soup.select('a.sb_pagN')
        if nextPageEle:
            url = nextPageEle[-1]['href']
            queryurl = urlparse.urljoin(queryurl, url)
            page += 1
        else:
            break
    return res

if __name__ == '__main__':
    for url in search(sys.argv[1:]):
        print url
