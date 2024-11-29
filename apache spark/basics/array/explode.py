from pyspark.sql import SparkSession
from pyspark.sql.functions import col,explode

spark = SparkSession.builder.appName("explode,split,array func explained").getOrCreate()

data = [(1,'vishu',['pyspark','sql']),(2,'rand1',['pyflink','sql'])]

schema = ['id','name','skills']

df = spark.createDataFrame(data,schema)

df.show()

# explode will create new row for every element

df1 = df.withColumn('skills',explode(col('skills')))

df1.show()