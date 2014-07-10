import sys
import json
from pprint import pprint

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #sent_file = open("AFFIN-111.txt")
    read_affin()
    tweet_file = open(sys.argv[1])
    #print sys.argv[1]
    #print tweet_file
    tweet_data = tweet_file.readlines()
    tweets = read_tweets(tweet_data)
    print len(tweets)
    for tweet in tweets[10:16]:
        print tweet["text"].encode('utf-8')
    print tweets[10].keys()
    #print tweet_data
    #tweet = json.loads(tweet_data)
    #pprint(tweets[10])
    #print tweet_file.read()

def read_tweets(tweet_data):
    tweets = []
    #print tweet_data
    #print "num tweets " + str(len(tweet_data.split("\n")))
    print "num " + str(len(tweet_data))
    for line in tweet_data:
        #print line
        tweets.append(json.loads(line))
    return tweets

def read_affin():
    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary

if __name__ == '__main__':
    main()
