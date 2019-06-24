# NYC-Parking-Violation

The dataset can be found here: https://vgc.poly.edu/~juliana/courses/BigData2018/Data/parking-violations.tar.gz

1. Using MapReduce to explore NYC parking violations in Hadoop:

task1: Write a map-reduce job that finds all parking violations that have been paid, i.e., that do not
occur in open-violations.csv.

task2: Write a map-reduce job that finds the distribution of the violation types in
parking_violations.csv, i.e., for each violation code, the number of violations that have this code.

task3: Write a map-reduce job that finds the total and average amount due in open violations for each
license type.

task4: Write a map-reduce job that computes the total number of violations for vehicles registered in
the state of NY and all other vehicles. 

task5: Write a map-reduce job that finds the vehicle that has had the greatest number of violations
(assume that plate_id and registration_state uniquely identify a vehicle).

task6: Write a map-reduce job that finds the top-20 vehicles in terms of total violations (assume that
plate id and registration state uniquely identify a vehicle).

task7: In March 2016, the 5th, 6th, 12th, 13th, 19th, 20th, 26th, and 27th were weekend days (i.e.,
Sat. and Sun.).

task8: Write a map-reduce job that finds the distribution of terms for the Make and Color columns,
i.e., for each value in those columns, how many times they appear in the column. Hint: you can
use the wordcount algorithm we covered in class.

task9:  List any data quality issues you have encountered in the provided datasets in a text file called
data-quality-issues.txt


2. Using Spark to explore NYC parking violations:

For each task you will use both core Spark using RDDs and SparkSQL using DataFrames. 

task1: Write a Spark program that finds all parking violations that have been paid, i.e., that do not occur in openviolations.csv.

task2: Write a Spark program that finds the distribution of the violation types, i.e., for each violation code, the
number of violations that have this code.

task3: Write a Spark program that finds the total and average amount due in open violations for each license
type.

task4: Write a Spark program that computes the total number of violations for vehicles registered in the state of
NY and all other vehicles. 

task5: Write a Spark program that finds the vehicle that has had the greatest number of violations (assume that
plate_id and registration_state uniquely identify a vehicle).

task6: Write a Spark program that finds the top-20 vehicles in terms of total violations (assume that plate id and
registration state uniquely identify a vehicle).

task7: In March 2016, the 5th, 6th, 12th, 13th, 19th, 20th, 26th, and 27th were weekend days (i.e., Sat. and
Sun.). Write a Spark program that, for each violation code, lists the average number of violations with that code
issued per day on weekdays and weekend days. You may hardcode “8” as the number of weekend days
and “23” as the number of weekdays in March 2016.






