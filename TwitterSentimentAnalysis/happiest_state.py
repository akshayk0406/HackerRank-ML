__author__ = 'akshaykulkarni'

import sys
import json
import re

def inputTokenize(text):
    REGEX = re.compile(r" \s*")
    return [tok.strip() for tok in REGEX.split(text)]

def hw(sent_file,tweet_file):

    scores                      = {}
    states_count                = {}
    most_occurring_state_count  = 0
    most_occurring_state        = ""

    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)

    for line in tweet_file:
        json_object = json.loads(line)

        if 'user' in json_object and 'location' in json_object['user']:
            if 'text' in json_object:
                tokens  = inputTokenize(json_object['text'].encode('utf-8'))

                score       = 0
                for word in tokens:
                    if word in scores:
                        score   = score + scores[word]

                for key in states:
                    if states[key] in json_object['user']['location']:
                        if key not in states_count:
                            states_count[key] = score
                        else:
                            states_count[key] += score
            else:
                score       = 0

    for key in states_count:
        if states_count[key] > most_occurring_state_count:
            most_occurring_state_count  = states_count[key]
            most_occurring_state        = key

    print most_occurring_state

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)


if __name__ == '__main__':
    main()