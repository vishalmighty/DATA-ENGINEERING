from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("df.show() explained") \
        .config("spark.sql.adaptive.enabled", "false")\
            .getOrCreate()
            
data = [(1,"commment1 fskjfdlkdsjflksdj"),
        (2,"commment2 fskjfdlkdsjflksdj"),
        (3,"commment3 fskjfdlkdsjflksdj"),
        (4,"commment4 fskjfdlkdsjflksdj"),
        (5,"commment5 fskjfdlkdsjflksdj")]
schema = ['id','comments']

df = spark.createDataFrame(data,schema)

# df.show(truncate = False)
# df.show(truncate = 6)

df.show(n=2) # n - number of row to show

# df.show(truncate = False,vertical = True) # vertical means - every column is in separate row(next next)