import csv
from operator import index
from pathlib import Path 
import csv
from unicodedata import category

oh=Path.cwd()/"csv_reports"/"overheads-day-45.csv"

with oh.open(mode="r", encoding="UTF-8") as file:
    overheads=[]
    category=[]
    reader=csv.reader(file)
    next (reader)
    for line in reader:
        category.append(line[0])
        overheads.append(line[1])
        
highest=[]
for value in overheads:
    value=float(value)
    highest.append(value)

def check():
    largest=-1
    for each in (highest):
        if each>largest:
            largest=each
            index=(highest.index(largest))
    print('[HIGHEST OVERHEAD]',category[index],',',largest)

check()

