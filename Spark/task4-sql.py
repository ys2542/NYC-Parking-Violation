import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("task4-sql").config("spark.some.config.option", "some-value").getOrCreate()
park = spark.read.format('csv').options(header = 'true', inferschema = 'true').load(sys.argv[1])

park.createOrReplaceTempView("park")

result = spark.sql("SELECT registration_state, count(registration_state) AS num FROM (SELECT CASE WHEN park.registration_state LIKE 'NY' THEN 'NY' ELSE 'Other' END AS registration_state FROM park) GROUP BY registration_state")

result.select(format_string('%s\t%d', result.registration_state, result.num)).write.save("task4-sql.out", format = "text")
