#import modules
import fastf1
import argparse


parser = argparse.ArgumentParser(description="Ingest schedule data from API to data lake")
parser.add_argument("year", help="Year of the schedule")
parser.add_argument("tarLoc", help="Target location to dump the files on")

args = parser.parse_args()

year = int(args.year)
tarLoc = args.tarLoc

yearlySchedule = fastf1.get_event_schedule(year)
if len(yearlySchedule) != 0:
    print(f"Ingesting raw schedule for year {year}")
    try:
        yearlySchedule.to_parquet(f"{tarLoc}seasonCalender_{args.year}.parquet", index=False)
        print(f"File successfully created for the year {year} : {tarLoc}seasonCalender_{args.year}.parquet")
        exit(0)
    except:
        print(f"Failed to create file for the year {year} : {tarLoc}seasonCalender_{args.year}.parquet")
else:
    exit(1)