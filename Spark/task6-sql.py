import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("task6-sql").config("spark.some.config.option", "some-value").getOrCreate()
park = spark.read.format('csv').options(header = 'true', inferschema = 'true').load(sys.argv[1])

park.createOrReplaceTempView("park")

result = spark.sql("SELECT plate_id, registration_state, count(plate_id) AS num FROM park GROUP BY plate_id, registration_state ORDER BY num DESC, plate_id LIMIT 20") 

result.select(format_string('%s, %s\t%d', result.plate_id, result.registration_state, result.num)).write.save("task6-sql.out", format = "text")
