from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("json reader") \
        .config("spark.sql.adaptive.enabled", "false") \
        .getOrCreate()
df = spark.read.json(path="./files/multi_line_json.json",multiLine=True)
df.printSchema()
df.show()

# for multi like json  objects should be in a list orelse it will take only the first one

# to take all files in a folder with .json use ..../folder_name/*.json