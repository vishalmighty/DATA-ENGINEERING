# partition large dataset into smaller files based on one or more columns
from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("PartitionBy Example") \
    .getOrCreate()

# Create a sample DataFrame
data = [
    ("Alice", "HR", 3000),
    ("Bob", "IT", 4000),
    ("Charlie", "HR", 3500),
    ("David", "IT", 4500),
    ("Eva", "Finance", 5000)
]
columns = ["name", "department", "salary"]

df = spark.createDataFrame(data, columns)

# Write the DataFrame to disk, partitioned by 'department'
output_path = "/path/to/output"  # Replace with your desired output path
df.write \
    .partitionBy("department") \
    .mode("overwrite") \
    .parquet(output_path)

print(f"Data has been written to {output_path} partitioned by 'department'.")

# Stop the SparkSession
spark.stop()


# to read only specific partition
# Path to the partitioned data
partitioned_path = "/path/to/output"  # Replace with your output path

# Read data for a specific department (e.g., 'HR')
department = "HR"
specific_partition_path = f"{partitioned_path}/department={department}"

df_hr = spark.read.parquet(specific_partition_path)

# Show the filtered data
df_hr.show()
