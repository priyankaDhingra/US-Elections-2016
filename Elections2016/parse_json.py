__author__ = 'priyanka'
import csv
import re
import json

from itertools import combinations
from collections import defaultdict
import operator
hashmap = {}
NODE = {}
GROUP = ''
nodedata = {'nodes': [],'links': []}

def increment_GROUP():
    global GROUP
    GROUP = GROUP+1

COUNT = -1


def increment():
    global COUNT
    COUNT = COUNT+1


def cooccur (com,filename):
    # with open('Input/raw/'+filename, 'rb') as data_file:


    # linkfile = open('graph/'+filename.split('.')[0]+'_link.json', 'w')
    # nodefile = open('graph/'+filename.split('.')[0]+'_node.json', 'w')



    com_max = []
# For each term, look for the most common co-occurrent terms
    for t1 in com:
        t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)
        for t2, t2_count in t1_max_terms:
            com_max.append(((t1, t2), t2_count))
# Get the most frequent co-occurrences
            if t1 not in NODE:
                increment()
                NODE[t1] = COUNT
                node = {'name':t1, 'group':GROUP}
                nodedata['nodes'].append(node)

            if t2 not in NODE:
                increment()
                NODE[t2] = COUNT
                node2 = {'name':t2, 'group':GROUP}
                nodedata['nodes'].append(node2)

            link = {'source':NODE[t1],'target':NODE[t2],'weight':t2_count['weight']}
            nodedata['links'].append(link)

            # print (t1, t2), t2_count['weight']
                    # terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
                    # print(terms_max[:1])
    # json.dump(nodedata,nodefile)
    # json.dump(linkdata,linkfile)


    # json.dump(linkdata,hashtagfile)

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

hashtagfile = open('graph/hashtag.json', 'w')
filenames = ['completeBernie_Sanders_merge.csv', 'completeDonald_Trump_merge.csv',\
             'completeHillary_Clinton_merge.csv', 'completeJeb_Bush_merge.csv', 'completeTed_Cruz_merge.csv']
for f in filenames:

    a = f.split('complete')[1].split('_')
    GROUP = a[0]+' '+a[1]
    cooccuring_mat = coocurrence(f)
    # create_json(cooccuring_mat,f)
    if cooccuring_mat is not None:
        cooccur(cooccuring_mat,f)

json.dump(nodedata,hashtagfile)