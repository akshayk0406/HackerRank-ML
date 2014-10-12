__author__ = 'akshaykulkarni'

import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate(record[1],record)

def reducer(key, list_of_values):

    result      = []
    orders      = []
    result_items= []

    for value in list_of_values:
        if 'order' == value[0]:
            orders.append(value)
        else:
            result_items.append(value)

    for order in orders:
        for item in result_items:
            result.append(order+item)

    mr.emit((key, result))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)