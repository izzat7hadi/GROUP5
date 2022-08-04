from heapq import heapify
from http.client import GATEWAY_TIMEOUT
from http.cookies import BaseCookie
from statistics import mean
from textwrap import indent
from tkinter import Button
from urllib import response

import requests

def api_extractor() :

#making the api key as a variable so that the code could access to the data
    api_keys = "QL8Q3ZVY82Y2DS1F"
    #inserting the url as a variable and including the api key to access the data
    url = "https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey=" + api_keys
    #making a response variable 
    response = requests.get(url)
    info = response.json()
    last_week_date  = list(info['Time Series FX (Weekly)'].keys())[0]
    last_week_closing = info['Time Series FX (Weekly)'][last_week_date]['4. close']
    return float(last_week_closing)

print(api_extractor())


