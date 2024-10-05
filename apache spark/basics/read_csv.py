from pyspark.sql import SparkSession
import time

spark = SparkSession.builder \
    .appName("Read CSV Example") \
    .config("spark.sql.adaptive.enabled", "false") \
    .getOrCreate()
    
csv_file_path = "/Users/vishal/Downloads/flink_stmt_aug_11.csv"
# print("Check AQE here: ",spark.conf.get("spark.sql.adaptive.enabled")) # This need to be false orelse no. of jobs won't be same as expected


# Try running this one by one and see the stages and no. of jobs
# df = spark.read.csv(csv_file_path, header=True, inferSchema=True)
# df = spark.read.csv(csv_file_path, header=True, inferSchema=False)
df = spark.read.csv(csv_file_path, header=False, inferSchema=False) # job 0

# df.printSchema()

# Show the content of the DataFrame
df.show() # this is creating one job? job 1

time.sleep(120)

# Stop the Spark session - This will stop the cluster gracefully releasing all the resources in use
spark.stop()