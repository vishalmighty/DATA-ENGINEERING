from pyspark.sql import SparkSession
from pyspark.sql.functions import col,split

spark = SparkSession.builder.appName("split func explained").getOrCreate()

data = [(1,'vishu','pyspark,sql'),(2,'rand1','pyflink,sql')]

schema = ['id','name','skills']

df = spark.createDataFrame(data,schema)

df.show()

df1 = df.withColumn('skillsArray',split(col('skills'),','))

df1.show()