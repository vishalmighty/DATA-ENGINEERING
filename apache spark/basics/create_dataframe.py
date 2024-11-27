from pyspark.sql import SparkSession
from pyspark.sql.types import *
import time

spark = SparkSession.builder \
    .appName("Read CSV Example") \
    .config("spark.sql.adaptive.enabled", "false") \
    .getOrCreate()
print("Helloooo")    
# print(type(spark))
# print(dir(spark))
# print("~~~~~~")  
# print(help(spark.createDataFrame))

 
# to create dataframe

data  = [(1,'vishal'),(2,'random person1')]
df = spark.createDataFrame(data=data,schema=['id','name'])
# print(df) # this is not correct
# df.show()
# df.printSchema()


# to override datatypes/manual datatypes
schema = StructType([StructField(name='id',dataType=IntegerType()),StructField(name='name',dataType=StringType())])
df1 = spark.createDataFrame(data=data,schema=schema)
df1.show()
df1.printSchema()

# to creaet with dictionary(keys become column name)

data = [{'id':1,'name':'Vishu'},
        {'id':2,'name':'Rand1'}]