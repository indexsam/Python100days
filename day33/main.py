#!/usr/bin/env python

import requests
import datetime as dt
import smtplib
import time

# source https://sunrise-sunset.org/api

# https://www.latlong.net/

my_email = "obadanindexsam@gmail.com"
password = "xxxxxxxxxxx"

LAT = 51.507351
LON = -0.127758

parameters = {
 "lat": LAT,
 "lng": LON,
 "formatted": 0,
}



response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()


sunrise_hr = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hr =  data["results"]["sunset"].split("T")[1].split(":")[0]


def send_mail(message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="obadansam@gmail.com", 
                    msg=f"Subject: Satelite Alert!\n\n{message}")


    print(" ISS alert eMail sent successfully!!")




msg = "Look UP!! Satelite approaching!!!"
check = True



response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_lon = float(data["iss_position"]["longitude"])

def validate_night():
    
    today = dt.datetime.now()
    this_hr = today.hour

    return (0 <= this_hr <= int(sunrise_hr)) or (int(sunset_hr) <= this_hr <= 23)


def validate_proxy():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lon = float(data["iss_position"]["longitude"])
  
    return ((iss_lat - 5) <= LAT <=(iss_lat + 5)) and ((iss_lon - 5) <= LON <=(iss_lon + 5))



counter = 0
while check:
    time.sleep(10) # 6secs
    counter +=1

    if validate_night() and validate_proxy():
        send_mail(msg)
        check = False
    
    else:
        print("Scanning for Satelite")

    if counter == 5:
        print("Exiting the program")
        check=False


# BONUS: run the code every 60 seconds.
 
