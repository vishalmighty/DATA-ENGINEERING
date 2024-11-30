from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Joins Example").getOrCreate()

# Create DataFrame 1
data1 = [
    (1, "John", "HR"),
    (2, "Alice", "IT"),
    (3, "Bob", "Finance"),
]
columns1 = ["id", "name", "dept"]
df1 = spark.createDataFrame(data1, columns1)

# Create DataFrame 2
data2 = [
    (1, "USA"),
    (2, "UK"),
    (4, "India"),
]
columns2 = ["id", "country"]
df2 = spark.createDataFrame(data2, columns2)

# Show the input DataFrames
print("DataFrame 1:")
df1.show()

print("DataFrame 2:")
df2.show()

inner_join = df1.join(df2, df1.id == df2.id, "inner")
print("Inner Join:")
inner_join.show()
