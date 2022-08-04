from pathlib import Path
import csv

from pkg_resources import empty_provider

pal=Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"

with pal.open(mode="r", encoding="UTF-8") as file:
    reader=csv.reader(file)
    for line in reader:
        print(line)

empty_list=[]
day_40= 558531
for cash in empty_list:
    if "41" < "40" :

        print(f"Day 41 Cash-on-Hand is lower than day 40 and the value difference is")
#if "558531" > "208706" 
print()