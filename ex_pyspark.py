from pyspark.sql import SparkSession 
spark = SparkSession.builder.master('local').appName('Test').getOrCreate()
print('Spark object is created')
rrd=spark.sparkContext.parallelsize([1,2,3])