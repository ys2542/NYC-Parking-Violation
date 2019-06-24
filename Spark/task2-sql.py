import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("task2-sql").config("spark.some.config.option", "some-value").getOrCreate()
park = spark.read.format('csv').options(header = 'true', inferschema = 'true').load(sys.argv[1])

park.createOrReplaceTempView("park")

result = spark.sql("SELECT violation_code, count(violation_code) AS num FROM park GROUP BY violation_code")

result.select(format_string('%d\t%d', result.violation_code, result.num)).write.save("task2-sql.out", format = "text")


