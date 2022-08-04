from heapq import heapify
from http.client import GATEWAY_TIMEOUT
from http.cookies import BaseCookie
from statistics import mean
from textwrap import indent
from tkinter import Button
from urllib import response

import requests
api_keys = "QL8Q3ZVY82Y2DS1F"
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_keys}"
response = requests.get(url)
info=response.json()
exchange=info["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
print(exchange)

#print (response)
#print(response.headers)
#print(response.headers.get('Content-Type'))
#data = response.json()
#print(type(data))
#print(data.keys())
#print(data)
#print(data["region_metadata"])
#print(data["items"])
#print(data["api_info"])
#import json
# print(json.dumps(data["items"],indent=4))
#pm25 = data["items"]
#print(len(pm25))
#pm_list = []
#for item in pm25:
    #print (item)
    #item["readings"]["pm25_one_hourly"].update({"timestamp": item["timestamp"]})
    #print(item["readings"]["pm25_one_hourly"])
    #pm_list.append(item["readings"]["pm25_one_hourly"])
    #item["readings"]["pm25_one_hourly"].update({"timestamp": item["timestamp"]})
   # pm_list.append(item["readings"]["pm25_one_hourly"])
#print(pm_list)



