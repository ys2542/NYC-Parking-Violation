import sys
from csv import reader
from pyspark import SparkContext

sc = SparkContext()
lines = sc.textFile(sys.argv[1], 1)
lines = lines.mapPartitions(lambda x: reader(x))

value_sum = lines.map(lambda x: (x[2], float(x[12])))
sum = value_sum.reduceByKey(lambda x, y: x + y)

value_count = lines.map(lambda x: (x[2], 1))
count =  value_count.reduceByKey(lambda x, y: x + y)

average = sum.join(count).map(lambda x: (x[0], x[1][0], float((x[1][0] / x[1][1]))))
output = average.map(lambda x: x[0] + '\t' + "{0:.2f}".format(x[1]) + ', ' + "{0:.2f}".format(x[2]))
output.saveAsTextFile("task3.out")
