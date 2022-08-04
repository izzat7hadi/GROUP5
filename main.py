import api, cash_on_hand, overheads, profit_loss
from pathlib import Path
import csv

def main():
    forex=api.api_extractor()
    cash_on_hand.Daily_checker(forex)
    profit_loss.check(forex)
    overheads.check2(forex)

main()
final=Path.cwd()/"final.csv"
final.touch
with final.open(mode="a",encoding="UTF-8",newline="") as file:
    empty_list=[]
    empty_list.append(cash_on_hand)
    empty_list.append(profit_loss)
    empty_list.append(overheads)
    
    writer=csv.writer(file)
    writer.writerow(empty_list)
    file.close()
