from pyspark.sql import SparkSession

# Step 1: Initialize SparkSession
spark = SparkSession.builder \
    .appName("createOrReplaceTempView Example") \
    .getOrCreate()

# Step 2: Create a sample DataFrame
data = [
    (1, "John", 5000),
    (2, "Jane", 6000),
    (3, "Mike", 7000)
]
columns = ["id", "name", "salary"]

df = spark.createDataFrame(data, columns)

# Step 3: Register the DataFrame as a temporary view
df.createOrReplaceTempView("employees")

# Step 4: Run SQL queries on the temporary view
result = spark.sql("SELECT id, name, salary FROM employees WHERE salary > 5500")

# Step 5: Show the result
result.show()
