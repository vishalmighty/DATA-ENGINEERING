from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import col, row_number, rank, dense_rank

# Initialize Spark session
spark = SparkSession.builder.appName("Ranking Functions").getOrCreate()

# Sample data
data = [
    ("Alice", "Math", 90),
    ("Alice", "English", 85),
    ("Bob", "Math", 95),
    ("Bob", "English", 80),
    ("Charlie", "Math", 95),
    ("Charlie", "English", 70),
]
columns = ["student", "subject", "score"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Define a window specification (partition by subject, order by score descending)
window_spec = Window.partitionBy("subject").orderBy(col("score").desc())

# Apply row_number, rank, and dense_rank
df_with_ranks = (
    df.withColumn("row_number", row_number().over(window_spec))
      .withColumn("rank", rank().over(window_spec))
      .withColumn("dense_rank", dense_rank().over(window_spec))
)

# Show results
df_with_ranks.show()
