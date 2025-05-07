# usage
# spark-submit schedule_transformer.py DD-MM-YYYY /path/to/config/file.config

#import modules
from pyspark.sql import SparkSession
import argparse

# creating a spark session
spark = SparkSession.builder.appName("schedule_transformer").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

#parse arguments
parser = argparse.ArgumentParser(description="Transform and load raw data for schedule of the next year")
parser.add_argument("date", help="date in DD-MM-YYYY format")
parser.add_argument("configFile", help="Path to configuration file")
args = parser.parse_args()

#assign arguments to varilables
year = int(args.date[-4:])+1 #extract year from argument
configFile = args.configFile

#logging
print(f"INFO: Running for the year {year}")
print(f"INFO: config file location {configFile}")

print(f"INFO: Reading config file...")
#read config file
try:
    with open(configFile, 'r') as file:
        config_lines = [line.strip() for line in file if line.strip()]
        config_vals = {}
        for l in config_lines:
            key,value = l.split('|')
            if key == 'source_file_pattern':
                value = value.replace("{year}",str(year))
            config_vals[key] = value
            if key == 'postgres_password' or key == 'postgres_user_name':
                # Do not print sensitive information
                continue
            print(f"INFO: {key} = {value}")
except Exception as e:
            print(f"ERROR: Failed to read the config file {configFile}")
            print(f"Error: {e}")
#adding date to pattern
#config_vals[source_file_pattern]=config_vals[source_file_pattern].replace("{year}",str(year))

#read raw file
raw_df = spark.read.option("sep", config_vals["delimiter"]) \
               .option("header", True) \
               .schema(config_vals["input_ddl"]) \
               .csv(f"{config_vals["source_path"]}/{config_vals["source_file_pattern"]}")

#create a temp view for querying
raw_table_name = "schedule_raw"
raw_df.createOrReplaceTempView(raw_table_name)

#reading property file and performing transform and load
print("INFO: Starting transformation and loading...")
with open(config_vals["property_file"], 'r') as file:
    property_lines = [line.strip() for line in file if line.strip()]  # Use a separate variable
    for l in property_lines:
        target_table, sql_query = l.split('|')
        sql_query = sql_query.replace("{raw_table}", raw_table_name)
        print(f"INFO: Running query for table {target_table}")
        try:
            # Execute the SQL query and write the output to the target table
            output = spark.sql(sql_query)
            output.write \
                .format("jdbc") \
                .option("url", "jdbc:postgresql://postgres_f1:5432/formula1") \
                .option("dbtable", target_table) \
                .option("user", config_vals["postgres_user_name"]) \
                .option("password", config_vals["postgres_password"]) \
                .option("driver", "org.postgresql.Driver") \
                .mode("append") \
                .save()
            print(f"INFO: Data loaded successfully for table {target_table} for the year {year}")
        except Exception as e:
            print(f"ERROR: Failed to load data for table {target_table} for the year {year}")
            print(f"Error: {e}")

print("INFO: Transformation and loading successfully completed.")
# Stop the Spark session
spark.stop()