#!/usr/bin/env python

from twilio.rest import Client
import requests
import json

# https://apilist.fun/  (explore APIs for fun projects)

api_key = "6b79814xxxxxxxxxxxxxxxxx"

 
# Convert timestamp to datetime
# dt_object = datetime.datetime.fromtimestamp(timestamp)

# Good source   https://www.ventusky.com/

#  Moccow , Lagos , Regina
LAT =  55.751244      # 6.451140        # 50.445210 
LON = 37.618423       # 3.388400        # -104.618896

parameters ={
   "lat": LAT,
   "lon": LON,
   "appid": api_key,
   "cnt": 4,
}


account_sid = 'AC4195a0axxxxxxxxxxxxxxxxxxxx'
auth_token = '34413xxxxxxxxxxxxxxxxxxxxxxxxx'


response = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

take_umbrella = False

for forcast in data["list"]:
    if forcast["weather"][0]["id"] < 700:
        print(f"Take an Umbrella!!!,  forcast for {forcast['dt_txt']}")
        take_umbrella=True

if take_umbrella:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                        from_='+12513166402',
                          to='+2347068000524',
                         body="Take an Umbrella!!")


