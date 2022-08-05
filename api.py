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
    #making a response variable to send request to get data from the url
    response = requests.get(url)
    #keeping the response which is a json data as info
    info = response.json()
    #making a variable for last weeks' date as list with info for time series fx weekly with api key
    last_week_date  = list(info['Time Series FX (Weekly)'].keys())[0]
    #making a variable for last week closing as info with time series fx weekly together with last weeks' date and the header for closing price in data
    last_week_closing = info['Time Series FX (Weekly)'][last_week_date]['4. close']
    #calling out the variable as a float
    return float(last_week_closing)
#calling out the entire code
print(api_extractor())


