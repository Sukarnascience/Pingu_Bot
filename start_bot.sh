#!/bin/bash

# Log current date and time
date >> Documents/pingu_bot/report.log
echo "Script started" >> Documents/pingu_bot/report.log

cd 
cd Documents/pingu_bot
echo "Changed directory" >> report.log

source env_for_bot/bin/activate
echo "Activated virtual environment" >> report.log

cd src
echo "Python script starts executing" >> report.log
python3 display01_stats.py
echo "Python script executed" >> report.log

