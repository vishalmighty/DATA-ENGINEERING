# extract elements from json string column and create new columns
from pyspark.sql import SparkSession
from pyspark.sql.functions import json_tuple

spark = SparkSession.builder \
    .appName("json_tuple Example") \
    .getOrCreate()

data = [
    (1, '{"name": "Alice", "age": 30, "city": "New York"}'),
    (2, '{"name": "Bob", "age": 40, "city": "San Francisco"}')
]

columns = ["id", "json_data"]

df = spark.createDataFrame(data, columns)

# Extract values from JSON string
df_extracted = df.select(
    "id",
    json_tuple("json_data", "name", "age", "city").alias("name", "age", "city")
)

df_extracted.show(truncate=False)