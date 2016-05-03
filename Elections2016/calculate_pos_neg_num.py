__author__ = 'priyanka'
import csv


def read_and_write_file(column_names):
    """Read in the json dataset file and write it out to a csv file, given the column names."""
    with open('graph/data.csv', 'w') as fout:
        csv_file = csv.writer(fout)
        csv_file.write(column_names)
        print column_names


def calculate_pos_neg_nu(filename):
    with open('Input/raw/'+filename, 'rb') as f:
        reader = csv.reader(f)
        num_neg_tweets = 0
        num_neutral_tweets = 0
        num_pos_tweets = 0

        for row in reader:
            try:
                if row[2] != 'Polarity':
                    if row[2] == '':
                        num_neutral_tweets += 1
                    elif float(row[2]) > 0.0:
                        num_pos_tweets += 1
                    elif float(row[2]) < 0.0:
                        num_neg_tweets += 1
                    else:
                        num_neutral_tweets += 1
            except ValueError as e:
                print (e , filename)
        a = filename.split('complete')[1].split('_')
        GROUP = a[0]+' '+a[1]
        return((GROUP,num_pos_tweets, num_neutral_tweets, num_neg_tweets))


filenames = ['completeBernie_Sanders_merge.csv', 'completeDonald_Trump_merge.csv',\
             'completeHillary_Clinton_merge.csv', 'completeJeb_Bush_merge.csv', 'completeTed_Cruz_merge.csv']
with open('graph/data.csv', 'w') as fout:
    csv_file = csv.writer(fout)
    csv_file.writerow(('Candidate','Positive','Neutral','Negative'))
    for f in filenames:
        csv_file.writerow(calculate_pos_neg_nu(f))