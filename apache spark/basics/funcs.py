from pyspark.sql import SparkSession
from pyspark.sql.functions import when

spark = SparkSession.builder.appName("when otherwise func explained").getOrCreate()

data = [(1,'M',23),
        (2,'F',24),
        (3,'',20)]
schema = ['id','gender','age']
df = spark.createDataFrame(data,schema)

# alias
df1 = df.select(df.id.alias('stud_id'))
df1.show()

# asc() & desc()
df1 = df.sort(df.gender.asc())
df1.show()

#cast()
df1 = df.select(df.id.cast('int'),df.gender)
df1.printSchema()

# like()
df1 = df.filter(df.gender.like('M%'))
df1.show()

# where/filter both are same
df.filter(df['age'] > 18).show()
df.filter(df.age > 18).show()
df.filter("age > 18").show()  # String expression

df.where(df['age'] > 18).show()
df.where(df.age > 18).show()
df.where("age > 18").show()  # String expression
