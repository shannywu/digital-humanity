#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import json
from itertools import izip
from Segmentor import Segmentor

if __name__ == '__main__':
    segmentor = Segmentor()
    for year in range(2010, 2017):
        posts = json.load(open('news_and_story/news_{0}.json'.format(year)))
        for post in posts:
            for line in post['content']:
                line = line.strip()
                # if line.startswith('CURRENT URL'):
                #     continue
                if line:
                    words = segmentor.segment(line)
                    print ' '.join(words).encode('utf-8')
