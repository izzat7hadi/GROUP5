from pathlib import Path
import csv

pal=Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"

with pal.open(mode="r", encoding="UTF-8") as file:
    reader=csv.reader(file)
    for line in reader:
        print(line)

empty_list=[]
