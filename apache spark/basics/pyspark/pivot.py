# pivot - to rotate data in one column to multiple columns
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName("Pivot Example").getOrCreate()

# Sample data
data = [
    (1, "John", "Male", "HR"),
    (2, "Alice", "Female", "IT"),
    (3, "Bob", "Male", "Finance"),
    (4, "Eve", "Female", "HR"),
    (5, "Tom", "Male", "IT"),
]
columns = ["id", "name", "gender", "dept"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Show the input DataFrame
print("Input DataFrame:")
df.show()

df.groupBy('dept','gender').count().show()

# Pivot the DataFrame based on gender, counting the number of employees in each department by gender
pivot_df = df.groupBy("dept").pivot("gender").count()

print("Pivoted DataFrame:")
pivot_df.show()

# to only pivot selected values
pivot_df = df.groupBy("dept").pivot("gender",['Male']).count()