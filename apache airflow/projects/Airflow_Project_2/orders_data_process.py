from pyspark.sql import SparkSession
import argparse

def main(date):
    # Create a Spark session
    spark = SparkSession.builder.appName("DataprocOrderProcessing").getOrCreate()

    # Define the path where the files are located
    input_path = f"gs://airflow-projects/airflow-project-2/data/orders_{date}.csv"
    
    # Read CSV files
    df = spark.read.csv(input_path, header=True, inferSchema=True)

    # Filter the records which got completed
    df_filtered = df.filter(df.order_status == "Completed")

    # Write back to GCS with the date naming convention
    output_path = f"gs://airflow-projects/airflow-project-2/output/processed_orders_{date}"
    df_filtered.write.csv(output_path, mode="overwrite", header=True)

    spark.stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process date argument')
    parser.add_argument('--date', type=str, required=True, help='Date in yyyymmdd format')
    args = parser.parse_args()
    
    main(args.date)