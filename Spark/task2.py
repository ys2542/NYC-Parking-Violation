import sys
from csv import reader
from pyspark import SparkContext

sc = SparkContext()
lines = sc.textFile(sys.argv[1], 1)
lines = lines.mapPartitions(lambda x: reader(x))

violation = lines.map(lambda x: (x[2], 1)).reduceByKey(lambda x, y: x + y)
output = violation.map(lambda x: x[0] + '\t' + str(x[1]))
output.saveAsTextFile("task2.out")
