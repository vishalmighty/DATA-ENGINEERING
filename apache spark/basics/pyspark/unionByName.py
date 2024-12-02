# unionByName - merge two df with different no of columns/diff schema by passing allowMissingColumns = True

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("when unionByName func explained").getOrCreate()

data1 = [(1,'M',1000),
        (2,'F',4000),
        (3,'F',2000),
        (4,'M',5000)]
schema1 = ['id','gender','salary']

data2 = [(1,'CSE',1000),
        (2,'IT',4000),
        (3,'CSE',2000),
        (4,'ECE',5000)]
schema2 = ['id','dept','salary']

df1 = spark.createDataFrame(data1,schema1)
df2 = spark.createDataFrame(data2,schema2)

df1.union(df2).show() # even schema is different this will work. Since order & datatype is same
# but the same will fail in unionByName
# df1.unionByName(df2).show() # this will throw error
df1.unionByName(df2,allowMissingColumns = True).show()
