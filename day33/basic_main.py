#!/usr/bin/env python

import requests
import json

# source http://open-notify.org/Open-Notify-API/ISS-Location-Now/

# https://www.latlong.net/


response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

print(json.dumps(data, indent=4))
