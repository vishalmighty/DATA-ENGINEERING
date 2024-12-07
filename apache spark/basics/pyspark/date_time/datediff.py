from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, current_date, datediff, months_between, add_months, date_add, year, month

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Date Functions Examples") \
    .getOrCreate()

# In Python, a single value enclosed in parentheses (e.g., ("2024-12-05")) is not treated as a tuple. Instead, it's treated as the value itself within parentheses (essentially the same as writing "2024-12-05"). To create a tuple with one element, a comma must be included after the value: ("2024-12-05",).
# Create a DataFrame with a single date column
data = [("2024-12-05",), ("2023-06-15",), ("2022-01-01",)]
columns = ["input_date"]
df = spark.createDataFrame(data, columns)

# Convert the input date to a date type
df = df.withColumn("input_date", col("input_date").cast("date"))

# Add current date column
df = df.withColumn("current_date", current_date())

# 1. datediff: Difference in days between two dates
df = df.withColumn("days_difference", datediff(col("current_date"), col("input_date")))

# 2. months_between: Difference in months between two dates
df = df.withColumn("months_difference", months_between(col("current_date"), col("input_date")))

# 3. add_months: Add or subtract months from a date
df = df.withColumn("add_3_months", add_months(col("input_date"), 3))  # Add 3 months
df = df.withColumn("subtract_2_months", add_months(col("input_date"), -2))  # Subtract 2 months

# 4. date_add: Add days to a date
df = df.withColumn("add_10_days", date_add(col("input_date"), 10))

# 5. Extract year and month from the input date
df = df.withColumn("year", year(col("input_date")))
df = df.withColumn("month", month(col("input_date")))

# Show the results
df.show(truncate=False)

# Stop Spark session
spark.stop()
