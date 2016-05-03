__author__ = 'priyanka'
import blockspring
import re
import pandas as pd
import csv


def find_polarity_by_url(url):
    polarity = blockspring.runParsed("sentiment-analysis-from-url-with-alchemyapi", \
    { "url":url , "score_only": True }, {"api_key":"br_30151_58a0e12e4ade73883d4ce599098f8126d34387e2"}).params.values()
    print polarity
    return polarity
# with open('Input/raw/completeHillary_Clinton_senti.csv', 'rb') as f, \
#         open('Input/raw/completeHillary_Clinton_merge.csv', 'wb') as tempfile:
# with open('Input/raw/completeJeb_Bush_senti.csv', 'rb') as f, \
#         open('Input/raw/completeJeb_Bush_merge.csv', 'wb') as tempfile:
with open('Input/raw/completeDonald_Trump_senti.csv', 'rb') as f, \
        open('Input/raw/completeDonald_Trump_merge.csv', 'wb') as tempfile:
# with open('Input/raw/completeBernie_Sanders_senti.csv', 'rb') as f, \
#         open('Input/raw/completeBernie_Sanders_merge.csv', 'wb') as tempfile:
# with open('Input/raw/completeTed_Cruz_senti.csv', 'rb') as f, \
#         open('Input/raw/completeTed_Cruz_merge.csv', 'wb') as tempfile:
    reader = csv.reader(f)
    writer = csv.writer(tempfile)
    for row in reader:

        if row[2] == '0.0':
            #print row[1]
            url = re.search("(?P<url>https?://[^\s]+)", row[1])

            if url is not None:
                newurl = url.group("url")
                writer.writerow([row[0],row[1],find_polarity_by_url(newurl),row[3]])
            else:
                writer.writerow(row)
        else:
            writer.writerow(row)



