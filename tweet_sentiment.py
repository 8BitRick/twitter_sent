import sys
import json
from pprint import pprint

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

# Thoughts about the approach
# ===========================
# Load in the word sentiment dictionary
# Load in the tweets
# for each tweet
#     If the tweet line is not a tweet then score is 0
#     else (it is a tweet!)
#         // Add up the sentiment of each word in the tweet
#         for each word
#             if word is NOT in wsd then score is 0
#             else get wsd[word] => should return a score
#             // Is there a pythonian way to do the test and score adding in one line?
#     print score from tweet
# // Done - assignment just wants the results printed

def main():
    # Get the sentiment file
    scores = read_affin(sys.argv[1] if (len(sys.argv) > 1) else 'AFINN-111.txt')

    # Get our tweets
    tweet_file = open(sys.argv[2] if (len(sys.argv) > 2) else 'output.txt')
    tweets = read_tweet_file(tweet_file)
    # Read each tweet
    for tweet in tweets:#[40:50]:
        score = 0
        # Make sure it is a tweet
        if 'text' in tweet:
            # Get the score for every word
            # print tweet["text"].encode('utf-8')
            for word in (tweet["text"].encode('utf-8').split()):
                # print word
                score += scores[word] if word in scores else 0
        print score

def read_tweet_file(tweet_file):
    tweet_data = tweet_file.readlines()
    return read_tweets(tweet_data)

def read_tweets(tweet_data):
    tweets = []
    # print "num " + str(len(tweet_data))
    for line in tweet_data:
        tweets.append(json.loads(line))
    return tweets

def read_affin(afinnfile_name):
    afinnfile = open(afinnfile_name)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items()[0:10] # Print every (term, score) pair in the dictionary
    return scores


if __name__ == '__main__':
    main()
