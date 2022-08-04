
from pathlib import Path
import csv

pal=Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
with pal.open(mode="r",encoding="UTF-8") as file:
    netprof=[]
    reader=csv.reader(file)
    for line in reader:
        netprof.append(line)
    
def check(data):
    deficit=[]

    days=list(index[0] for index in data[1:])
    profit_loss=list(float(index[4]) for index in data[1:])
    
    for index in range(len(days)):
        if (index==0) or (index==len(days)-1):
            continue
        if profit_loss[index]<profit_loss[index-1]:
            diff=profit_loss[index] - profit_loss[index-1]
            deficit.append([days[index],diff])
            day=days[index]
            diff=abs(diff)
    print(f"[PROFIT DEFICIT] DAY:{day}, AMOUNT: SGD{diff}")
check(netprof)

    

