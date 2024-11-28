# this is a transformation function
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,lit

spark = SparkSession.builder.appName("with column func explained").getOrCreate()

data = [(1,2000),
        (2,3000)] 
columns = ['id','salary']

df = spark.createDataFrame(data,schema = columns)
df.printSchema()

df1 = df.withColumn(colName='salary',col=col('salary').cast('Integer'))

df1.show()
df1.printSchema()

df2 = df1.withColumn(colName='new_salary',col=col('salary')*2)

df2.show()


df3 = df1.withColumn(colName='country',col=lit('India'))

# lit will return col type data

df3.show()