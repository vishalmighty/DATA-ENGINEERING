from pyspark.sql import SparkSession,dataframe


spark = SparkSession.builder \
    .appName('read csv') \
    .config("spark.sql.adaptive.enabled", "false") \
    .getOrCreate()

# print(help(dataframe))

data = [(1,"vish"),(2,"rand1")]
schema = ['id','name']
df = spark.createDataFrame(data=data,schema=schema)

df.write.csv(path='/Users/vishal/Documents/GitHub/DATA-ENGINEERING/apache spark/basics/test',header=True) # this will write in multiple files due to parallelism of worker nodes

#mode = overwrite , ignore , append, error