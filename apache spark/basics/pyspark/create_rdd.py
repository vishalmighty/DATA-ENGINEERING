data = [(1,'vishu'),(2,'rand')]

rdd = spark.sparkContext.parallelize(data)
print(rdd.collect())


# convert rdd to dataframe
df = rdd.toDF()
df = rdd.toDF(scehma=['id','name'])

df = spark.createDataFrame(rdd,schema=['id','name'])

# to convert dataframe to rdd

df.rdd.functions
df.rdd.map