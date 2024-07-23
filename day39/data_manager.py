#!/usr/bin/env python

import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get("https://api.sheety.co/515c6df7305f0adbc9e22a2096c204dd/copyOfFlightDeals/prices")
        self.response.raise_for_status()
        self.result = self.response.json()
        self.data = self.result["prices"]

