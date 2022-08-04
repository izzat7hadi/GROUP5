import csv
from hashlib import new
from operator import index
from pathlib import Path 
import csv
from pickle import APPEND
import string
from unicodedata import category
#to open files from folder
oh=Path.cwd()/"csv_reports"/"overheads-day-45.csv"
#using reading mode to read files
with oh.open(mode="r", encoding="UTF-8") as file:
    overheads=[]
    category=[]
    reader=csv.reader(file)
    next (reader)
    for line in reader:
        #using append to add elements to the list
        category.append(line[0])
        overheads.append(line[1])
 #creating new list to find       
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
    print(f"[HIGHEST OVERHEAD] {category[index]} : {largest} %")

check()

