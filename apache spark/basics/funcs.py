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

#############################
# distinct - distinct of all columns df.distinct()
# dropDuplicates - distinct of one or multiple columns df.dropDuplicates(), df.dropDuplicates(['column1'])

#############################
# sort() & orderBy are same
# df.sort('id')
# df.sort(df.id)
# df.sort(df.id.desc())
# df.sort(df.name.desc(),df.id.desc())

# df.orderBy('id')

#############################
# union & unionAll - both are same, union will not work as sql/will not remove duplicates
# df3 = df1.union(df2)
#to remove duplicates
# df3.distinct()


#############################
# select syntax
# df.select('id','name')
# df.select(df.id,df.name)
# df.select(df['id'],df['name'])
# df.select(col('id'),...)
# df.select['id','name']
# df.select('*')
# df.select([col for col in df.columns]) # selects all columns

#############################
# df.fillna('unknown') -> all string columns with null rows are replaced by 'unknown'
# df.fillna('unknown',['col_name_1']) -> specified string columns with null rows are replaced by 'unknown'
# # df.na.fill() -> same as fill na

#############################
# sample() -> get  random sample from large dataset
# fraction -> what percentage of data
# seed -> value to make sure every time to get same random sample 
# if seed value is same then samples will also be same
# df1 = df.sample(random=0.1, seed=12)
# df2 = df.sample(random=0.1, seed=12)


#############################
# retrive all elements in a Dataframe as an Array if Row type to the driver node
# returns - array
# for big dataframe it may throw OOM error as it returns entire data to single node(driver)