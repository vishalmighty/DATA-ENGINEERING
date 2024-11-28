from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("with column renamed func explained").getOrCreate()


data = [(1,2000),
        (2,3000)] 
columns = ['id','salary']

df = spark.createDataFrame(data,schema = columns)


df1 = df.withColumnRenamed('salary','salary_renamed')
#or
# df  = df.withColumnRenamed('salary','salary_renamed')
#but dataframes are immutable

df1.show()
