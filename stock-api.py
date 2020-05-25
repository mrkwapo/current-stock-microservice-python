# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:56:29 2020

@author: Nate Kwapo
"""
#Eureka Discovery Server


#Flask
from flask import Flask
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json

app = Flask(__name__)

import py_eureka_client.eureka_client as eureka_client

your_rest_server_port = 9090
# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
eureka_client.init_registry_client(eureka_server="http://localhost:8761/,http://localhost:8761/eureka",
                                app_name="stock-api",
                                instance_port=5000)

@app.route('/stock/profile/<path:symbol>')
def getCompanyProfileData(symbol): 
    url = "https://financialmodelingprep.com/api/v3/company/profile/{}?apikey=5df07fe2e77eb907f2496af6f4a48260".format(symbol)
    
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


@app.route('/stock/quote/<path:symbol>')
def getStockQuoteData(symbol): 
    url = "https://financialmodelingprep.com/api/v3/quote/{}?apikey=5df07fe2e77eb907f2496af6f4a48260".format(symbol)

    response = urlopen(url)
    data = response.read().decode("utf-8")
    for item in json.loads(data):
        return item


@app.route('/stock/price/<path:symbol>')
def getStockPrice(symbol): 
    url = "https://financialmodelingprep.com/api/v3/quote-short/{}?apikey=5df07fe2e77eb907f2496af6f4a48260".format(symbol)
    
    response = urlopen(url)
    data = response.read().decode("utf-8")
    for item in json.loads(data):
        return item
    
