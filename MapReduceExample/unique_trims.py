__author__ = 'akshaykulkarni'

import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate(record[0],record[1][:-10])

def reducer(key, list_of_values):
    result = []
    for v in list_of_values:
        if v not in result:
          result.append(v)

    mr.emit((key,result))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
