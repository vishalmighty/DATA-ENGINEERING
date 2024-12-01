from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Step 1: Initialize SparkSession
spark = SparkSession.builder \
    .appName("UDF Example") \
    .getOrCreate()

# Step 2: Create a sample DataFrame
data = [
    (1, "John", 5000),
    (2, "Jane", 6000),
    (3, "Mike", 7000)
]
columns = ["id", "name", "salary"]

df = spark.createDataFrame(data, columns)

# Step 3: Define a UDF to transform data
def add_prefix(name):
    return f"Employee: {name}"

# Register the UDF
add_prefix_udf = udf(add_prefix, StringType())

# Step 4: Apply the UDF on the 'name' column
df_with_prefix = df.withColumn("name_with_prefix", add_prefix_udf(df["name"]))

# Step 5: Show the result
df_with_prefix.show()
