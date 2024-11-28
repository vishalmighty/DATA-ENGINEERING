# under testing
from pyflink.table import EnvironmentSettings, TableEnvironment, CsvTableSource
from pyflink.table.descriptors import Schema, FileSystem, OldCsv
import time

# Create the TableEnvironment
env_settings = EnvironmentSettings.new_instance().in_batch_mode().build()
table_env = TableEnvironment.create(env_settings)

# Path to the CSV file
csv_file_path = "/Users/vishal/Downloads/flink_stmt_aug_11.csv"

# Define the schema and register the CSV file as a source
table_env.connect(FileSystem().path(csv_file_path)) \
    .with_format(OldCsv()
                 .field_delimiter(",")  # Set delimiter (default is ',')
                 .line_delimiter("\n")  # Line break
                 .field("col1", "STRING")  # Define fields
                 .field("col2", "STRING")
                 .field("col3", "INT")    # Adjust based on your CSV structure
                 ) \
    .with_schema(Schema()
                 .field("col1", "STRING")
                 .field("col2", "STRING")
                 .field("col3", "INT")) \
    .create_temporary_table("csv_source")

# Query the registered table
table = table_env.from_path("csv_source")

# Convert to DataStream (optional if you need to use the DataStream API)
data_stream = table_env.to_append_stream(table)

# Print the content of the table
print("Schema:")
table.print_schema()

print("Content:")
result = table_env.execute_sql("SELECT * FROM csv_source")
result.print()  # This shows the contents of the table

# Introduce sleep to mimic delays
time.sleep(120)

# No explicit stop in Flink as Flink jobs typically run continuously.
