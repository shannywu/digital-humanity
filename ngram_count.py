#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import json
from itertools import izip
from collections import Counter
from operator import itemgetter
from Segmentor import Segmentor
from nltk.corpus import stopwords

eng_symbols = '{}"\'()[].,:;+!?-*/&|<>=~$'
ch_symbols = u'，。、；：！？「」（）『』～”…《》＼｜／【】'

eng_stopwords = set(stopwords.words('english'))
ch_stopwords = set(map(lambda x: x.strip().decode('utf-8').split()[0], open('ch.stopwords.txt')))

MAX_DISTANCE = 5


def ngram_is_valid(ngram):
    first, last = ngram[0], ngram[-1]
    if first in eng_stopwords or last in eng_stopwords:
        return False
    if first in ch_stopwords or last in ch_stopwords:
        return False
    if any(num in first or num in last for num in '0123456789'):
        return False
    if any(symbol in word for word in ngram for symbol in eng_symbols):
        return False
    if any(symbol in word for word in ngram for symbol in ch_symbols):
        return False
    return True


def to_ngrams(unigrams, length):
    return izip(*[unigrams[i:] for i in range(length)])

if __name__ == '__main__':
    # segmentor = Segmentor()
    ngram_counter = Counter()

    for i, line in enumerate(fileinput.input()):
        line = line.strip().decode('utf-8')

        # words = segmentor.segment(line)
        words = line.split()
        for n in range(1, MAX_DISTANCE+1):
            ngram_counter.update(filter(ngram_is_valid, to_ngrams(words, n)))
            # ngram_counter.update(to_ngrams(words, n))

    for ngram, count in ngram_counter.most_common():
        print u'{}\t{}'.format(' '.join(ngram), count).encode('utf-8')
