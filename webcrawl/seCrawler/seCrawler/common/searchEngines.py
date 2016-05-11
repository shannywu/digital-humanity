SearchEngines = {
    'google': 'https://www.google.com/search?q={0}&start={1}&lr=lang_zh-TW&cr=countryTW',
    'bing': 'http://www.bing.com/search?q={0}&first={1}&rf=1',
    'baidu': 'http://www.baidu.com/s?wd={0}&pn={1}'
}


SearchEngineResultSelectors = {
    'google': '//div//h3/a/@href',
    'bing': '//li[@class="b_algo"]//h2/a/@href',
    'baidu': '//h3/a/@href',
}
