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
    #create 2 empty lists to append data inside it
    overheads=[]
    category=[]
    #reading the file
    reader=csv.reader(file)
    #skipping first row as it is not a number
    next (reader)
    #for loop to reiterate every element
    for line in reader:
        #using append to add elements to the list
        category.append(line[0])
        overheads.append(line[1])
#creating new list to store finalised data      
highest=[]
for value in overheads:
    #float so that it can be used in calculation
    value=float(value)
    highest.append(value)
#creating function to find max
def check2():

    largest=-1
    #reiterate over all elements in list
    for each in (highest):
        #using this to find the max
        if each>largest:
            largest=each
            #using index to find the position of the wanted value
            index=(highest.index(largest))
    print(f"[HIGHEST OVERHEAD] {category[index]} : {largest} %")

check2()

