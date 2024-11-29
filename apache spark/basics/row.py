from pyspark.sql import Row, SparkSession

# row is extenstion of tuple

spark = SparkSession.builder.appName("maptype func explained").getOrCreate()

# Accessing rows
row = Row('vishu',1000)
print(row[0])
row = Row(name = 'vishu',salary = 1000)
print(row.name)

# Creating dataframe from row

row1 = Row(name = 'vishu',salary = 1000)
row2 = Row(name = 'rand1',salary = 2000)

data = [row1,row2]
df = spark.createDataFrame(data)
df.show()

# above we created row objects, now lets create row like class

Person = Row('name','salary')
p1 = Person('vishu',3000)
p2 = Person('randy',4000)

print(p1.name)