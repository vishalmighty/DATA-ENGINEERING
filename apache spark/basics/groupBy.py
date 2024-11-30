from pyspark.sql import SparkSession
from pyspark.sql.functions import min,count,max

spark = SparkSession.builder.appName("when groupBy func explained").getOrCreate()

data = [(1,'M','CSE',1000),
        (2,'F','IT',4000),
        (3,'F','CSE',2000),
        (4,'M','ECE',5000)]
schema = ['id','gender','dept','salary']
df = spark.createDataFrame(data,schema)

df1 = df.groupBy(df.dept).count()
df1.show()

df1 = df.groupBy(df.dept,df.gender).count()
df1.show()

df1 = df.groupBy(df.dept).min('salary') # can't pass salary as object , here min only accepts string
df1.show()

# aggregate function
df1 = df.groupBy(df.dept).agg(count('*').alias('countOfStud'),min(df.salary)) # but here we can pass both string and object
df1.show()