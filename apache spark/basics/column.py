from pyspark.sql import SparkSession
from pyspark.sql.functions import lit,col

spark = SparkSession.builder.appName("maptype func explained").getOrCreate()
data = [(1,2),(3,4)]
df = spark.createDataFrame(data)

# lit funtion explained
df1 = df.withColumn('new_column',lit('newdata'))
df1.show()

# Access columns in multiple ways from a dataframe
df.select(df.col_name).show()
df.select(df['col_name']).show()
df.select(col('col_name')).show()

# Access struct column
df.select(df.col_name.sub_col_name).show()
df.select(df['col_name.sub_col_name']).show()
df.select(col('col_name.sub_col_name')).show()