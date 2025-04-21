from pyspark.sql import SparkSession


# Correct way to create SparkSession with app name
spark = SparkSession.builder.appName("Hello world").getOrCreate()

# Read the text file
df = spark.read.option("sep", "<#??#>") \
               .option("header", True) \
               .csv("/data/scheduling_raw/seasonCalender_2020.txt")



# Show the first 10 rows
df.select(['RoundNumber','F1ApiSupport']).show(10)

# Stop the Spark session
spark.stop()
