# Project Formula 1

PF1 aims to give Formula 1 enthusiasts insights into Formula 1. This project shows schedules, car telemetry, driver performance over his career in Formula, and more. As this project develops, it will try to predict a race outcome.

# Installation and setup

Run git clone on your computer to download the project:
```
git clone https://github.com/nikhileshjo/formula1-data.git
```

After downloading, create a python virtual environment and install the dependencies
```
python -m venv my_env
#change environment after this
pip install -r requirements.txt
```
Now, you're ready to load the weekly results of a race
```
python ingestion_scripts/ingest.py <year> <session>
```
replace year with the year and session with session number.

That's all, you can keep refreshing the PowerBi dashboard to see freshly updated results.
(note: The PowerBI refresh will work only if your path to the source is like this:
D:\projects\formula1-data\ingestion_scripts\ingest.py you might have to rebuild the dashboard if you want a refresh)