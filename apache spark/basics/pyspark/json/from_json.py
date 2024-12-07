# converts json string to MapType or StructType
#json to map
data = [
    ("1", '{"key1":"value1", "key2":"value2"}'),
    ("2", '{"keyA":"valueA", "keyB":"valueB"}')
]

# Define schema
schema = ["id", "json_string"]

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Define the MapType schema
map_schema = MapType(StringType(), StringType())

# Convert JSON string to MapType column
df_with_map = df.withColumn("map_column", from_json(col("json_string"), map_schema))

#############
# json string to struct type
data = [
    ("1", '{"name":"Alice", "age":30}'),
    ("2", '{"name":"Bob", "age":40}')
]

# Define schema
schema = ["id", "json_string"]

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Define the StructType schema
struct_schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# Convert JSON string to StructType column
df_with_struct = df.withColumn("struct_column", from_json(col("json_string"), struct_schema))


##########
# convert map/struct type to json string
# to_json()

data = [
    (1, {"key1": "value1", "key2": "value2"}, {"name": "Alice", "age": 30}),
    (2, {"key1": "value3", "key2": "value4"}, {"name": "Bob", "age": 40})
]

# Define schema
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("map_col", MapType(StringType(), StringType()), True),
    StructField("struct_col", StructType([
        StructField("name", StringType(), True),
        StructField("age", IntegerType(), True)
    ]), True)
])

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Convert MapType and StructType columns to JSON strings
df_with_json = df.withColumn("map_as_json", to_json(col("map_col"))) \
                 .withColumn("struct_as_json", to_json(col("struct_col")))