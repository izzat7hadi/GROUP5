import csv
from operator import index
from pathlib import Path 
import csv
from unicodedata import category

pal=Path.cwd()/"csv_reports"/"overheads-day-45.csv"

with pal.open(mode="r", encoding="UTF-8") as file:
    empty_list=[]
    reader=csv.reader(file)
    for line in reader:
        empty_list.append(line)
<<<<<<< HEAD

def main(data):
    highest=[]

    category = list(index[0] for index in data[1:])
    overheads = list((index[1]) for index in data [1:])
    highest.append([category,overheads])
   
    for index in range(len(category)):
     if (index==0):
            continue 
     largestvalue= -1
    
    for each in overheads :
          if each > largestvalue :
            largestvalue = each
            highest.append([overheads,largestvalue ])
    print(each)
main(empty_list) 
=======
    print(line)
>>>>>>> 850e156af8ee6ca43f5fc6cd0726930ce4aaf242

