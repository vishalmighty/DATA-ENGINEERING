from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType
from pyspark.sql.functions import col,array

spark = SparkSession.builder.appName("with column renamed func explained").getOrCreate()

data = [(1,("vishu","name1"),3000),(2,("rand1","name2"),2000)]

customtype = StructType([StructField(name='firstname',dataType=StringType()),
                         StructField(name='lastname',dataType=StringType())])

schema = StructType([StructField(name='id',dataType=IntegerType()),
                     StructField(name='name',dataType=customtype),
                     StructField(name='salary',dataType=IntegerType())])

df = spark.createDataFrame(data,schema)
# df.printSchema()
# df.show()


# array type

data = [(1,[2,3,4]),
        (2,[1,2,3])]

schema = StructType([StructField(name='id',dataType=IntegerType()),
                     StructField(name='numbers',dataType=ArrayType(IntegerType()))])

df = spark.createDataFrame(data,schema)

# df.printSchema()

# taking first ele from array

# df.withColumn('fistNumber',df.numbers[0]).show()


# combaining 2 ele into array

data = [(1,2),
         (3,4)]
schema = ['num1','num2']

df = spark.createDataFrame(data,schema)
df.withColumn('numbers_combined',array(col('num1'),col('num2'))).show()