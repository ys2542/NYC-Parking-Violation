import sys
from csv import reader
from pyspark import SparkContext

sc = SparkContext()
line_park = sc.textFile(sys.argv[1], 1)
line_park = line_park.mapPartitions(lambda x: reader(x))
line_open = sc.textFile(sys.argv[2], 1)
line_open = line_open.mapPartitions(lambda x: reader(x))

park = line_park.map(lambda x: (x[0], (x[14], x[6], x[2], x[1])))
open = line_open.map(lambda x: (x[0], ('', '', '', '')))

result = park.subtractByKey(park.join(open))
output = result.map(lambda x: x[0] + '\t' + x[1][0] + ', ' + x[1][1] + ', ' + x[1][2] + ', ' + x[1][3])
output.saveAsTextFile("task1.out")
