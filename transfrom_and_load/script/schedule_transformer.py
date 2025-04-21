#import modules
from pyspark.sql import SparkSession
import argparse

#parse arguments
parser = argparse.ArgumentParser(description="Transform and load raw data for schedule")
parser.add_argument("year", help="Year of the schedule")
parser.add_argument("configFile", help="Path ot configuration file")
args = parser.parse_args()

#assign arguments to varilables
year = int(args.year)
configFile = args.configFile

# creating a spark session
spark = SparkSession.builder.appName("schedule_transformer").getOrCreate()



# # Read the text file
# df = spark.read.option("sep", "<#??#>") \
#                .option("header", True) \
#                .csv(f"{}")