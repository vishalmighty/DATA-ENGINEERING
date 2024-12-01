# unpivot - to rotate columns into rows

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

# Initialize Spark session
spark = SparkSession.builder.appName("UnpivotExample").getOrCreate()

# Sample data
data = [
    (1, "Vishu", 90, 85, 88),
    (2, "Rand1", 78, 92, 81),
    (3, "Rand2", 85, 80, 79)
]

# Define the schema
columns = ["id", "name", "math", "science", "history"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Show the original DataFrame
df.show()

# Unpivot the DataFrame
unpivoted_df = df.selectExpr("id", "name", "stack(3, 'math', math, 'science', science, 'history', history) as (subject, score)")

# Show the unpivoted DataFrame
unpivoted_df.show()

########
## another method
# from pyspark.sql.functions import expr
# df.select('colum_name',expr("stack(no_of_columns_to_unpivot,'value1',column1,'value2',column2) as (col1,col2)"))
# df.select('department',expr("stack(2,'male',male,'female',female) as (gender,count)"))

# department | male | female
# converted to
# department | gender | count