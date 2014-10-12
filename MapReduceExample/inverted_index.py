__author__ = 'akshaykulkarni'

import MapReduce
import sys
import re

mr = MapReduce.MapReduce()

def inputTokenize(text):
    REGEX = re.compile(r" \s*")
    return [tok.strip() for tok in REGEX.split(text)]

def mapper(record):

    document_id = record[0]
    text        = record[1]

    tokens      = inputTokenize(text)
    for word in tokens:
        mr.emit_intermediate(word, [document_id])

def reducer(key, list_of_values):
    result = []
    for v in list_of_values:
      result.extend(v)

    mr.emit((key, result))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)