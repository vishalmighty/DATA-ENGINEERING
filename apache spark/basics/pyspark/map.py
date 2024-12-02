# dataframe doesn't support map fn only rdd supports it
# applys function(lambda) on every element of RDD and returns new RDD


# Create an RDD
numbers_rdd = spark.SparkContext.parallelize([1, 2, 3, 4, 5])

# Apply the map function to calculate the square of each number
squared_rdd = numbers_rdd.map(lambda x: x ** 2)
# or
# squared_rdd = numbers_rdd.map(lambda x: custom_func(x))

# Collect and print the results
squared_numbers = squared_rdd.collect()
print(f"Squared Numbers: {squared_numbers}")

