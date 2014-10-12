__author__ = 'akshaykulkarni'

import sys
import re
import json

def inputTokenize(text):
    REGEX = re.compile(r" \s*")
    return [tok.strip() for tok in REGEX.split(text)]

def hw(tweet_file):

    total_wc    = 0
    result      = {}
    for line in tweet_file:
        json_object = json.loads(line)
        if 'text' in json_object:
            tokens  = inputTokenize(json_object['text'].encode('utf-8'))
            for word in tokens:
                if word in result:
                    result[word]    = result[word] +1
                else:
                    result[word]    = 1

                total_wc            = total_wc  + 1

    for k,v in result.iteritems():
        print k, (v*1.0)/total_wc

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
