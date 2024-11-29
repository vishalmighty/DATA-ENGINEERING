from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, MapType

spark = SparkSession.builder.appName("array_contains func explained").getOrCreate()

data = [(1,'vishu',{'eye':'blue','hair':'black'}),(2,'rand1',{'eye':'white','hair':'black'})]
schema = ['id','name','characteristics']
df = spark.createDataFrame(data,schema)
df.show(truncate=False)

df1 = df.withColumn('eye',df.characteristics['eye'])

df1.show(truncate=False)

schema = StructType([StructField('id',IntergerType()),
                    StructField('name',StringType()),
                    StructField('characteristics',MapType(StringType(),StringType()))]
                    )