import csv
from hashlib import new
from operator import index
from pathlib import Path 
import csv
from pickle import APPEND
import string
from unicodedata import category

oh=Path.cwd()/"csv_reports"/"overheads-day-45.csv"

with oh.open(mode="r", encoding="UTF-8") as file:
<<<<<<< HEAD
    empty_list=[]
    category=[]
    reader=csv.reader(file)
    next(reader)
    
=======
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

>>>>>>> 2d04d4ac051d747a6fce75df80706c3d7f8b60d1
