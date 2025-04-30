![formula-1-car](img/formula-1-car.png)

# Project Formula 1

PF1 aims to give Formula 1 enthusiasts insights into Formula 1. This project shows schedules, car telemetry, driver performance over his career in Formula, and more. As this project develops, it will try to predict a race outcome.

# Installation and setup

The requirement for setting this up is that Docker be installed on your computer. Once you have that up and running

- save this repository in a location on your computer
- Open your terminal or command prompt inside the formula1-data directory
- Execute the below command

```bash
docker-compose -f init/docker-compose.yml up -d
```

Give it a couple of minutes, and it should start running.

Open your web browser and log on to: localhost:portnumber [Available after phase-1 completion]

# Project Structure

Below is a description of what the project folders and and what each of them contains:

- datalake: This folder contains the data that’s ingested by a Python script. This folder aims to act like a data lake that can consume raw data, and the data then sits there waiting to be consumed by the downstream. Note: the data is not deleted after downstream consumes it, so this could grow in size over time.
- img: This has images for the README.md
- ingestion_scripts: This contains ingestion scripts, which do API calls and dump the data in `datalake` folder in .txt format
- init: This has scripts that run when you spin up the docker container. They do some housekeeping to keep things clean and simple.
- transform_and_load: This contains pyspark scripts that clean and transform the raw data into whatever tabular format, so that it’s consumable by PostgreSQL tables (our data warehouse).

## Tools

For this project, we use:

- Docker: This keeps things simple and makes it OS agnostic. The housekeeping becomes simple. Also, when you don’t want the project to be on your computer anymore, it’s easy to clean it up.
- Apache Spark: This is our transformation tool. It is an overkill for the amount of data we’re handling, but this is also a portfolio project for a data engineer, so you can’t not have the most trending tool in the industry.
- Python: This is used to create the transformation scripts for Apache Spark, and also vanilla monolithic Python for data ingestion.
- PostgreSQL: This is our data warehousing tool. This was chosen because it keeps things simple and is freely available. It also favours the Kimball way of data warehousing.
- Apache Airflow: This is our orchestration tool to automate the entire process. (yet to set up)