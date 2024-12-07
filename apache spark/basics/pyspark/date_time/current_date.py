from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_date, date_format, to_date

# Initialize Spark session
spark = SparkSession.builder \
    .appName("PySpark Date Functions Example") \
    .getOrCreate()

# Create a DataFrame using range
# Generates a DataFrame with a single column 'id' containing values from 0 to 9
df = spark.range(10).toDF("id")

# Add a column with the current date
df = df.withColumn("current_date", current_date())

# default format is yyyy-MM-dd
# Format the current_date column to a specific format (e.g., 'dd-MM-yyyy')
df = df.withColumn("formatted_date", date_format(col("current_date"), "dd-MM-yyyy"))

# Convert a string to a date using to_date
# Simulating a string date for demonstration
df = df.withColumn("string_date", date_format(col("current_date"), "yyyy-MM-dd"))
df = df.withColumn("converted_date", to_date(col("string_date"), "yyyy-MM-dd"))

# Show the results
df.show(truncate=False)

# Stop Spark session
spark.stop()
