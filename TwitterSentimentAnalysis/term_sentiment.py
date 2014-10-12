import sys
import re
import json

def inputTokenize(text):
    REGEX = re.compile(r" \s*")
    return [tok.strip() for tok in REGEX.split(text)]

def get_unique_terms(scores,tweets):

    unique_terms    = []
    for tweet in tweets:
        for word in tweet[0]:
            if word not in scores:
                unique_terms.append(word)

    return set(unique_terms)

def score_terms(unique_terms,tweets):

    '''
    Filter out terms with lenght greater than 2
    '''

    req_terms   = {term:[0,0] for term in unique_terms if len(term) > 2}

    for tweet in tweets:
        for word in tweet[0]:
            if word in req_terms:
                req_terms[word][0]  = req_terms[word][0] + tweet[1]
                req_terms[word][1]  = req_terms[word][1]

    return {key : (req_terms[key][0]*1.0)/(req_terms[key][1]) for key in req_terms}

def hw(sent_file,tweet_file):

    scores          = {}
    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)


    tweets         = []
    for line in tweet_file:
        json_object = json.loads(line)
        if 'text' in json_object:
            tokens  = inputTokenize(json_object['text'].encode('utf-8'))

        score       = 0
        for word in tokens:
            if word in scores:
                score   = score + scores[word]

        tweets.append((tokens,score))


    unique_terms    = get_unique_terms(scores,tweets)
    result          = score_terms(unique_terms,tweets)

    for key in result:
        print key , result[key]

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)

if __name__ == '__main__':
    main()
