from pyspark.sql import SparkSession
from pyspark.sql.functions import col,explode, map_keys, map_values


spark = SparkSession.builder.appName("maptype func explained").getOrCreate()

data = [(1,'vishu',{'eye':'blue','hair':'black'}),(2,'rand1',{'eye':'white','hair':'black'})]
schema = ['id','name','characteristics']
df = spark.createDataFrame(data,schema)

df1 = df.select('id','name',explode(df.characteristics))
# to print keys and values each separately in one column

df1.show(truncate=False)

# to get only keys
df1 = df.select('id','name',map_keys(df.characteristics))
df1.show()

# to get only values
df2 = df.select('id','name',map_values(df.characteristics))
df2.show()