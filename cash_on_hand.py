from pathlib import Path
import csv
import api
coh=Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"

empty_list = []

with coh.open(mode="r", encoding="UTF-8") as file:
    reader=csv.reader(file)
    for line in reader:
        empty_list.append(line)
       
#print(url_creator('USD','SGD'))
#curency = url_creator('USD','SGD')
#print(currency['Realtime Currency Exchange Rate']['5. Exchange Rate'])


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
