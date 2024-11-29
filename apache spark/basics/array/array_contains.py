from pyspark.sql import SparkSession
from pyspark.sql.functions import col,array_contains

spark = SparkSession.builder.appName("array_contains func explained").getOrCreate()

data = [(1,'vishu',['pyspark','sql']),(2,'rand1',['pyflink','sql'])]

schema = ['id','name','skills']

df = spark.createDataFrame(data,schema)

df.show()

df1 = df.withColumn('Has_pyflink_skill',array_contains(col('skills'),'pyflink'))

df1.show()