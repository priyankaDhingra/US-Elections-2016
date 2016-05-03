__author__ = 'priyanka'
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from textblob import TextBlob
from threading import Thread
import time
from pandas import *
import csv, codecs
import json
import datetime

atoken = "1317760776-l6Mttz4UtynxZd6s2vyixP8e4cdnPFRABNuWUw1"
asecret = "0Mr0pnNGYONOxVB8rv9wIjALeSwBb220iJsCgQqwRQNv9"
ckey = "JV5B5b6L7DrSyenhltzQLuOOD"
csecret = "XL02wHHoRVqqoLqmfDf5HLVd4clN8bh2uCpz5AGr0u36irVNCm"
class Listener(StreamListener):
    def __init__(self, name, path=None):
        self.name = name
        #We'll need this later.
        self.path = path

    def on_data(self, data):
        try:
            all_data = json.loads(data)
            tweet = all_data["text"]
            username = all_data["user"]["screen_name"]
            print((username,tweet))


            #Open, write and close your file.
            savefile = open('Input/raw/'+ self.name.replace(' ', '_')+'.json', 'ab')
            savefile.write(tweet.decode('utf-8'))
            savefile.close()

            #Open, write and close your file.
            savefile = open('Input/raw/complete'+ self.name.replace(' ', '_')+'.json', 'ab')
            savefile.write(data.decode('utf-8'))
            savefile.close()
            return True
        except BaseException as e:
                print('failed ondata,', str(e))
                time.sleep(5)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, Listener('Ted Cruz'))
tweets = twitterStream.filter(track=['Ted Cruz'],languages=['en'])
# twitterStream = Stream(auth, Listener('Hillary Clinton'))
# tweets = twitterStream.filter(track=['Hillary Clinton'],languages=['en'])
# twitterStream = Stream(auth, Listener('Donald Trump'))
# tweets = twitterStream.filter(track=['Donald Trump'],languages=['en'])
# twitterStream = Stream(auth, Listener('Jeb Bush'))
# tweets = twitterStream.filter(track=['Jeb Bush'],languages=['en'])
# twitterStream = Stream(auth, Listener('Bernie Sanders'))
# tweets = twitterStream.filter(track=['Bernie Sanders'],languages=['en'])