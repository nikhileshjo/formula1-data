#import modules
import fastf1
import argparse
import os

# Instantiate input arguments. This will allow us to give input through our scheduler
parser = argparse.ArgumentParser(description="Ingest schedule data from API to data lake")
parser.add_argument("year", help="Year of the schedule")
parser.add_argument("tarLoc", help="Target location to dump the files on")

args = parser.parse_args()

# assigning arguments to easy to use variables
year = int(args.year)
tarLoc = args.tarLoc

#fetching schedule
print(f"Fetching schedule for the year {year}")
try:
    yearlySchedule = fastf1.get_event_schedule(year)
    print(f"Successfully fetched the schedule for the year {year}")
except Exception as e:
    print(f"Failed to get the schedule for the year {year}")
    print(f"Error: {e}")

if len(yearlySchedule) != 0:
    print(f"Ingesting raw schedule for year {year}")
    try:
        file_path = os.path.join(tarLoc, f"seasonCalender_{args.year}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            # Write header
            f.write("<#??#>".join(yearlySchedule.columns) + "\n")
            # Write each row
            for _, row in yearlySchedule.iterrows():
                f.write("<#??#>".join(map(str, row.values)) + "\n")

        print(f"File successfully created for the year {year} : {file_path}")
    except Exception as e:
        print(f"Failed to create file for the year {year} : {file_path}")
        print(f"Error: {e}")
else:
    exit(1)
