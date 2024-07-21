#!/usr/bin/env python

import requests
from dotenv import load_dotenv
import os

# load the .env file
load_dotenv()


APP_ID=os.getenv("APP_ID")
API_KEY2=os.getenv("API_KEY2")



DOMAIN ="https://trackapi.nutritionix.com"
ENDPOINT = "/v2/natural/exercise"

input_params ={
"query": input("Tell me what exercise you did? ")

}

headers={
'x-app-id':APP_ID,
'x-app-key':API_KEY2,

}


response = requests.post(f"{DOMAIN}{ENDPOINT}", json=input_params, headers=headers)
response.raise_for_status()
data = response.json()

#  working with google sheets via sheety 

import datetime as dt

date_time = dt.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
list_date_time = date_time.split()
Datepart = list_date_time[0]
Timepart = list_date_time[1]


# optinoal and resetable
headers = {
"Authorization": "Basic aW5kZXhzYW06c2FtaWNlMktAMQ",

}


for dict_activity in data["exercises"]:
    
    params = {
    "workout": {
	"date": Datepart,
	"time": Timepart,
         "exercise":dict_activity["name"].title() ,
         "duration": dict_activity["duration_min"],
          "calories": dict_activity["nf_calories"],
       }
     } 
     
    response = requests.post("https://api.sheety.co/515c6df7305f0adbc9e22a2096c204dd/copyOfMyWorkouts/workouts", json=params) #, headers=headers)
    response.raise_for_status()
    print(response.text)


