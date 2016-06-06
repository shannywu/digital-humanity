#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
from collections import defaultdict
from itertools import izip


filterset = {u'清大', u'清華'}


def parse_ngram_count(line):
    line = line.strip().decode('utf-8')
    ngram, count = line.split('\t')
    ngram = tuple(ngram.split())
    count = int(count)
    return ngram if len(ngram) > 1 else ngram[0], count

if __name__ == '__main__':

    ngram_dict = dict(map(parse_ngram_count, fileinput.input()))
    nodes = set()
    # node_dict = {word[0]: i for i, word in
    #              enumerate(filter(lambda x: len(x) == 1, ngram_dict.keys()))}

    edge_dict = defaultdict(int)
    for ngram, count in ngram_dict.iteritems():
        if count < 10:
            continue
        if not any(word in filterset for word in ngram):
            continue
        for bigram in izip(*[ngram[i:] for i in range(2)]):
            edge_dict[bigram] = max(edge_dict[bigram], count)

    for (source, target), count in edge_dict.iteritems():
        nodes.update([source, target])

    # output node
    print 'Id,Count'
    for node in nodes:
        if node not in ngram_dict:
            continue
        print u'{0},{1}'.format(node, ngram_dict[node]).encode('utf-8')

    # output edge
    # print 'Source,Target,Count'
    # for (source, target), count in edge_dict.iteritems():
    #     print u'{0},{1},{2}'.format(source, target, count).encode('utf-8')
