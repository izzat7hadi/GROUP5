import api, cash_on_hand, overheads, profit_loss

def main():
    cash_on_hand.Daily_checker()
    api.api_extractor()
    profit_loss.check()
    overheads.check2()

main()
