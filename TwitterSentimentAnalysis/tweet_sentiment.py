import sys
import json
import re

def inputTokenize(text):
    REGEX = re.compile(r" \s*")
    return [tok.strip() for tok in REGEX.split(text)]

def hw(sent_file,tweet_file):

    scores          = {}
    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)

    for line in tweet_file:
        json_object = json.loads(line)
        if 'text' in json_object:
            tokens  = inputTokenize(json_object['text'].encode('utf-8'))

        score       = 0
        for word in tokens:
            if word in scores:
                score   = score + scores[word]
        print score

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)

if __name__ == '__main__':
    main()
