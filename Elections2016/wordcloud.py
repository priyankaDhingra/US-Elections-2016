__author__ = 'priyanka'
from nltk.corpus import stopwords
import string
import re
import csv
import json

from collections import Counter
FREQ = {'frequents': []}

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


def wordcloud(filename):
    with open('Input/raw/'+filename, 'r') as f:
        punctuation = list(string.punctuation)
        stop = stopwords.words('english') + punctuation + ['rt', 'via']

        count_all = Counter()
        reader = csv.reader(f)
        for row in reader:
        # Create a list with all the terms
            #terms_all = [term for term in preprocess(row[1])]
            terms_all = [term for term in preprocess(row[1]) \
                if term not in stop and \
                not term.startswith(('#', '@'))]
        # Update the counter
            count_all.update(terms_all)

    for k, v in count_all.items():
        FREQ['frequents'].append({'text':k, 'size': v})

    # Print the first 5 most frequent words
    a = filename.split('complete')[1].split('_')
    GROUP = a[0]+' '+a[1]
    jsonfile = open('graph/'+GROUP+'.json','wa')
    json.dump(FREQ,jsonfile)
    print(count_all.most_common(5))

filenames = ['completeBernie_Sanders_merge.csv']
#, 'completeDonald_Trump_merge.csv',\             'completeHillary_Clinton_merge.csv', 'completeJeb_Bush_merge.csv', 'completeTed_Cruz_merge.csv']
for f in filenames:
    wordcloud(f)