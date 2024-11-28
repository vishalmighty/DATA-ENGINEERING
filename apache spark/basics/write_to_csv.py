from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName('read csv') \
    .config("spark.sql.adaptive.enabled", "false") \
    .getOrCreate()
