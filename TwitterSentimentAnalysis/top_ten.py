__author__ = 'akshaykulkarni'

import sys
import re
import json
import operator

def inputTokenize(text):
    REGEX = re.compile(r" \s*")
    return [tok.strip() for tok in REGEX.split(text)]

def hw(tweet_file):

    result          = {}
    for line in tweet_file:
        json_object = json.loads(line)

        if 'text' in json_object:
            tokens  = inputTokenize(json_object['text'].encode('utf-8'))

            for word in tokens:
                if len(word) > 0 and '#' == word[0]:

                    if word in result:
                        result[word]    = result[word]+1
                    else:
                        result[word]    = 1

    sorted_result       = sorted(result.items(), key=operator.itemgetter(1) ,reverse=True)
    i                   = 0

    for k,v in sorted_result:
        print k,v

        i   = i +1
        if i == 10:
            break


def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
