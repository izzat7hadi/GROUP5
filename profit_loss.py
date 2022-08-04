
from pathlib import Path
import csv

pal=Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
with pal.open(mode="r",encoding="UTF-8") as file:
    empty_list=[]
    reader=csv.reader(file)
    for line in reader:
        empty_list.append(line)
    
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
        
    print(deficit)
check(empty_list)

    #data=empty_list
    #emplist=[]
    #for prof in data:
        #emplist.append(prof[4])
    
    #for netprof in emplist:
        #floatprof=float(netprof)
        #diff= floatprof[2]-floatprof[2-1]
        #print(floatprof)
      
        #def prof(number):

            
            #if diff<0:
                #print(f"PROFIT DEFICIT, {diff}")





        
        #if cash_diff<0:
            #print(f"[NET PROFIT DEFICIT]] day")
        
    
        

        