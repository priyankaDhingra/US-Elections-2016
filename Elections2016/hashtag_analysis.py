__author__ = 'priyanka'
import csv
import re
import json

from itertools import combinations
from collections import defaultdict
import operator


def cooccur (com,filename):
    with open(filename.split('.')[0]+'hashtag.json', 'w') as outfile:
        com_max = []
        # For each term, look for the most common co-occurrent terms
        for t1 in com:
            t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)
        for t2, t2_count in t1_max_terms:
            data = [{'source': t1, 'target': t2, 'weight': t2_count}]
            # Get the most frequent co-occurrences
            print data
            json.dump(data, outfile)


def coocurrence (filename):
    with open('Input/raw/'+filename, 'rb') as f:

        com = defaultdict(lambda : defaultdict(lambda: {'weight':0}))
        reader = csv.reader(f)

        for row in reader:
            x = re.compile(r'\B#\w*[a-zA-Z]+\w*')
            terms_only = x.findall(row[1])
            # Build co-occurrence matrix
            for w1, w2 in combinations(sorted(terms_only), 2):
                if w1 != w2:
                    com[w1][w2]['weight'] += 1
        return com


def create_json(com, filename):
    with open(filename.split('_')[1]+'_hashtag.json', 'wa') as outfile:
        json.dump(com, outfile)

filenames = ['completeBernie_Sanders_merge.csv', 'completeDonald_Trump_merge.csv',\
             'completeHillary_Clinton_merge.csv', 'completeJeb_Bush_merge.csv', 'completeTed_Cruz_merge.csv']
for f in filenames:
    cooccuring_mat = coocurrence(f)
    create_json(cooccuring_mat,f)
    # if cooccuring_mat is not None:
    #     cooccur(cooccuring_mat,f)
