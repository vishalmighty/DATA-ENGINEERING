from pyspark.sql import SparkSession
from pyspark.sql.functions import udf,col
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


### another method

# Step 3: Define UDFs using @udf decorator
@udf(returnType=StringType())
def add_prefix(name):
    return f"Employee: {name}"

@udf(returnType=DoubleType())
def double_salary(salary):
    return salary * 2

# Step 4: Apply the UDFs on DataFrame
df_with_udfs = df \
    .withColumn("name_with_prefix", add_prefix(col("name"))) \
    .withColumn("doubled_salary", double_salary(col("salary")))

# Step 5: Show the result
df_with_udfs.show()

# also we can use this registered function in sql syntax