from sklearn.naive_bayes import GaussianNB
import sys
import re

def inputTokenize(text):
    REGEX = re.compile(r" \s*")
    return [tok.strip() for tok in REGEX.split(text)]


def readfile(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield inputTokenize(line)


filepath = 'trainingdata.txt'
lines_in_file = readfile(filepath)
total_lines = 0
total_words = 0
word_dictionary = {}
idx = 0
Y = []
X = []

for line in lines_in_file:
    if 1 == len(line):
        total_lines = int(line[0])

    else:
        Y.append(int(line[0]))
        for word in line[1:]:
            if len(word) > 0 and word not in word_dictionary:
                word_dictionary[word] = idx
                idx = idx + 1
        X.append(" ".join(line[1:]))

for i in range(0, len(X)):

    vector = [0] * len(word_dictionary)
    tokens = inputTokenize(X[i])
    for word in tokens:
        if len(word) > 0 and word in word_dictionary:
            vector[word_dictionary[word]] = 1
    X[i] = vector

gaussianModel = GaussianNB()
model = gaussianModel.fit(X, Y)

test_input  = sys.stdin.readlines()
tc = int(test_input[0])

init_word_dictionary    = [0] * len(word_dictionary)
ans                     = [0] * tc

for i in range(tc):
    inp = test_input[i]
    tokens = inputTokenize(inp)
    vector = init_word_dictionary

    for word in tokens:
        if len(word) > 0 and word in word_dictionary:
            vector[word_dictionary[word]] = 1

    ans[i]  =   model.predict(vector)[0]

print ans

'''
model = OneVsRestClassifier(LinearSVC(random_state=0))
model.fit(data, Y)

print model.coef_

ans = []
feature_vector_dict = {}

for word in feature_name:
    feature_vector_dict[word] = 0

tc = int(raw_input())

for i in range(tc):

    inp = raw_input()
    tokens = inputTokenize(inp)

    frequency_dict = feature_vector_dict
    for word in tokens:
        if word in feature_vector_dict:
            frequency_dict[word] = frequency_dict[word] + 1

    ans.append(model.predict(frequency_dict.values()))

for result in ans:
    print result[0]

'''
