import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("task3-sql").config("spark.some.config.option", "some-value").getOrCreate()
ov = spark.read.format('csv').options(header = 'true', inferschema = 'true').load(sys.argv[1])

ov.createOrReplaceTempView("ov")

result = spark.sql("SELECT license_type, SUM(amount_due) AS total, AVG(amount_due) AS average FROM ov GROUP BY license_type")

result.select(format_string('%s\t%.2f, %.2f', result.license_type, result.total, result.average)).write.save("task3-sql.out", format = "text")
