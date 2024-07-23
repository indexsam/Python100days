#!/usr/bin/env python

from pprint import pprint


'''
This file will need to use the 
DataManager,FlightSearch, FlightData, 
NotificationManager classes to achieve the program requirements.
'''
import requests

from data_manager import DataManager
from flight_search import FlightSearch

#sheet_data = DataManager()
# pprint(sheet_data.data)

data  = sheet_data.data



params = {
  "price": {

    "iataCode": "TESTING"
  }
}


for dict_data in data:
    response =requests.put(f"https://api.sheety.co/515c6df7305f0adbc9e22a2096c204dd/copyOfFlightDeals/prices/{dict_data['id']}", json=params)
    print(response.text)
