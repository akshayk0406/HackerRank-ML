from sklearn.svm import LinearSVC
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
import sys
import re

tc      = sys.stdin.readline().strip()
tokens  = tc.split(" ")
n,m     = int(tokens[0]),int(tokens[1])


trn     = 0.6*n
ten     = 0.4*n
Id      = []

Xtrain  = []
Ytrain  = []

Xtest   = []
Ytest   = []

for i in xrange(n):
    inp     = sys.stdin.readline().strip()
    tokens  = inp.split(" ")

    Id.append(tokens[0])

    if i < trn:
        Ytrain.append(tokens[1])
    else:
        Ytest.append(tokens[1])

    feature_vector  = [0.0]*m
    for j in range(2,m+2):

        Tokens              = tokens[j].split(":")
        feature_vector[j-2] = float(Tokens[1])

    if i < trn:
        Xtrain.append(feature_vector)
    else:
        Xtest.append(feature_vector)


Xtrain              = preprocessing.scale(Xtrain)
Xtest               = preprocessing.scale(Xtest)

C                   = [0.1,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
best_c              = 1
best_model          = 0
best_minclassify    = 1000000000

for c in C:
    model   = LinearSVC(C=c).fit(Xtrain,Ytrain)
    ans     = model.predict(Xtest)

    misclassificatons   = 0
    for i in xrange(len(ans)):
        if int(Ytest[i]) != int(ans[i]):
            misclassificatons   = misclassificatons+1

    if best_minclassify > misclassificatons:
        best_minclassify    = misclassificatons
        best_c              = c
        best_model          = model

'''
gaussianModel = GaussianNB()
best_model = gaussianModel.fit(Xtrain, Ytrain)

logreg              = linear_model.LogisticRegression(C=1)
logreg.fit(Xtrain,Ytrain)
'''


inp                 = int(sys.stdin.readline())
for i in xrange(inp):

    sample      = sys.stdin.readline()
    tokens      = sample.split(" ")
    Id          = tokens[0]

    feature_vector  = [0.0]*m
    for j in range(1,m+1):

        Tokens              = tokens[j].split(":")
        feature_vector[j-1] = float(Tokens[1])

    result      = best_model.predict(feature_vector)
    print Id , result[0]
