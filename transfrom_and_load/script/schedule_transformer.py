#import modules
from pyspark.sql import SparkSession
import argparse

# creating a spark session
spark = SparkSession.builder.appName("schedule_transformer").getOrCreate()

#parse arguments
parser = argparse.ArgumentParser(description="Transform and load raw data for schedule of the next year")
parser.add_argument("date", help="date in DD-MM-YYYY format")
parser.add_argument("configFile", help="Path ot configuration file")
args = parser.parse_args()

#assign arguments to varilables
year = int(args.date[-4:])+1 #extract year from argument
configFile = args.configFile

#logging
print(f"Running for the year {year}")
print(f"config file location {configFile}")

print(f"Reading config file...")
#read config file
with open(configFile, 'r') as file:
    config_lines = [line.strip() for line in file if line.strip()]
    config_vals = {}
    for l in config_lines:
        key,value = l.split('|')
        if key == 'source_file_pattern':
            value = value.replace("{year}",str(year))
        print(f"{key} = {value}")
        config_vals[key] = value

#adding date to pattern
#config_vals[source_file_pattern]=config_vals[source_file_pattern].replace("{year}",str(year))

#read raw file
raw_df = spark.read.option("sep", config_vals["delimiter"]) \
               .option("header", True) \
               .csv(f"{config_vals["source_path"]}/{config_vals["source_file_pattern"]}")

#create a temp view for querying
raw_table_name = "schedule_raw"
raw_df.createOrReplaceTempView(raw_table_name)

#reading property file and performing transform and load
print("Starting transformationan and loading...")
with open(config_vals["property_file"], 'r') as file:
    config_lines = [line.strip() for line in file if line.strip()]
    config_vals = {}
    for l in config_lines:
        target_table,sql_query = l.split('|')
        sql_query =  sql_query.replace("{raw_table}",raw_table_name)
        print(f"Ingesting data for the table {target_table}")
        print(f"SQL: {sql_query}")
        #target_df = spark.sql(sql_query)


spark.stop()