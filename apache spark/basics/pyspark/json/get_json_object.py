from pyspark.sql import SparkSession
from pyspark.sql.functions import get_json_object, col

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("get_json_object Nested JSON Example") \
    .getOrCreate()

# Sample nested JSON data
data = [
    ('{"user": {"name": "Alice", "details": {"age": 25, "city": "New York"}}}',),
    ('{"user": {"name": "Bob", "details": {"age": 30, "city": "Los Angeles"}}}',),
    ('{"user": {"name": "Charlie", "details": {"age": 35, "city": "Chicago"}}}',)
]

# Define schema and create DataFrame
columns = ["json_data"]
df = spark.createDataFrame(data, columns)

# Extract nested JSON fields using get_json_object
df_with_extracted = df.select(
    col("json_data"),
    get_json_object(col("json_data"), "$.user.name").alias("name"),
    get_json_object(col("json_data"), "$.user.details.age").alias("age"),
    get_json_object(col("json_data"), "$.user.details.city").alias("city")
)

# Show the result
df_with_extracted.show(truncate=False)

# Stop Spark session
spark.stop()
