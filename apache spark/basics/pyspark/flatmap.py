# flatmap() - falttens RDD
# similar as explode(flatten arrays in dataframe) in dataframes



rdd = spark.SparkContext.parallelize([
    "Apache Spark is great",
    "PySpark makes big data easy",
    "FlatMap is powerful"
])

# Apply the flatMap function to split sentences into words
words_rdd = rdd.flatMap(lambda sentence: sentence.split(" "))

# Collect and print the results
words = words_rdd.collect()
print(f"Words: {words}")