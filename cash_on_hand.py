from pathlib import Path
import csv
<<<<<<< HEAD

from pkg_resources import empty_provider

=======
import api
<<<<<<< HEAD
coh=Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
=======
>>>>>>> 850e156af8ee6ca43f5fc6cd0726930ce4aaf242
pal=Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
>>>>>>> 6f41263acb2c6d36f36fc0be80560b9e6f3c0864

empty_list = []

with coh.open(mode="r", encoding="UTF-8") as file:
    reader=csv.reader(file)
    for line in reader:
        empty_list.append(line)
       
#print(url_creator('USD','SGD'))
#curency = url_creator('USD','SGD')
#print(currency['Realtime Currency Exchange Rate']['5. Exchange Rate'])

<<<<<<< HEAD
empty_list=[]
day_40= 558531
for cash in empty_list:
    if "41" < "40" :

        print(f"Day 41 Cash-on-Hand is lower than day 40 and the value difference is")
#if "558531" > "208706" 
print()
=======

def Daily_checker(data):
    issues = []
    # Separate the data into two separate lists
    days = list(i[0] for i in data[1:])
    cash_on_hand = list(int(i[1]) for i in data[1:])

    ## Trying to determine if the next day is higher than current day
    for i in range(len(days)):
        ## Skip the first day and last day: this is a problem for python counting
        if (i ==0) or (i == len(days) - 1):
            continue
        # i is the current day and i-1 is the previous day
        ## Today is lesser than the previous day, we need to flag this out
        if cash_on_hand[i] <  cash_on_hand[i-1]:
            diff = cash_on_hand[i] - cash_on_hand[i-1]
            issues.append([days[i], diff])
    print(f"[CASH DEFICIT] DAY:{days[i]}, AMOUNT: SGD{abs(diff)}")
        
Daily_checker(empty_list)
>>>>>>> 850e156af8ee6ca43f5fc6cd0726930ce4aaf242
