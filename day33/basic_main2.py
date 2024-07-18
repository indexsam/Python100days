#!/usr/bin/env python

import requests
import json

# source http://open-notify.org/Open-Notify-API/ISS-Location-Now/

# https://www.latlong.net/


LAT = 50.429601
LON =-104.511356

parameters = {
 "lat": LAT,
 "lng": LON,
 "formatted": 1,
}



response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

print(json.dumps(data, indent=4))
