# This is same as case when
from pyspark.sql import SparkSession
from pyspark.sql.functions import when

spark = SparkSession.builder.appName("when otherwise func explained").getOrCreate()

data = [(1,'M'),
        (2,'F'),
        (3,'')]
schema = ['id','gender']
df = spark.createDataFrame(data,schema)

df1 = df.select(df.id,when(df.gender=='M','Male').when(condition=df.gender=='F',value='Female')\
    .otherwise('Unknown').alias('Gender'))

df1.show()
df1.printSchema()