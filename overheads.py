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
    empty_list=[]
    category=[]
    reader=csv.reader(file)
    next(reader)
    