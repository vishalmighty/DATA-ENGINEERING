from pyspark.sql import SparkSession
from pyspark.sql.functions import upper

# Step 1: Initialize SparkSession
spark = SparkSession.builder \
    .appName("Transform Example") \
    .getOrCreate()

# Step 2: Create a sample DataFrame
data = [
    (1, "Vishu", 5000),
    (2, "rand1", 6000),
    (3, "rand2", 7000)
]
columns = ["id", "name", "salary"]

df = spark.createDataFrame(data, columns)

# Step 3: Define transformation functions
def convertNameToUpper(df):
    return df.withColumn("name", upper(df["name"]))  # Convert name to uppercase

def doubleSalary(df):
    return df.withColumn("salary", df["salary"] * 2)  # Double the salary

# Step 4: Apply transformations using `transform`
df1 = df.transform(convertNameToUpper).transform(doubleSalary)

# Step 5: Show the result
df1.show()

##################################
# Another transform function
# pyspark.sql.fucntions.transform()
# applys transformation only on column type array and returns an object of ArrayType only

data = [
    (1, ["John", "Jane", "Mike"], [5000, 6000, 7000]),
    (2, ["Alice", "Bob", "Carol"], [8000, 9000, 10000])
]
columns = ["id", "names", "salaries"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Apply transformation using transform function
transformed_df = df.withColumn(
    "names_uppercase",
    transform(col("names"), lambda x: upper(x))  # Change names to uppercase
).withColumn(
    "salaries_doubled",
    transform(col("salaries"), lambda x: x * 2)  # Double the salaries
)

# Show the result
transformed_df.show(truncate=False)
