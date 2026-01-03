import fastf1 as ff
from pathlib import Path
import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("arg1")
parser.add_argument("arg2")

args = parser.parse_args()

def save_result(path_to_file, df):
    output_path = Path(path_to_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

year = int(args.arg1)
session_cnt = int(args.arg2)

try:
    session = ff.get_session(year, session_cnt, 'R')
    session.load(laps=True, telemetry=False, weather=False, messages=False, livedata=None)
    res = session.results[['ClassifiedPosition','Abbreviation','DriverNumber','Time', 'Status','TeamName', 'Points']]
    res["load_date"] = datetime.date.today()
    path_to_file = f"ingested_data/results.csv"
    save_result(path_to_file, res)
    print(f"INFO: year={year} and session number={session_cnt} loaded successfully.")
    print("INFO: Load completed!")
except:
    print(f"ERROR: No session with year={year} and session number={session_cnt}")

