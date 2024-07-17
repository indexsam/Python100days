#!/usr/bin/env python

import smtplib
import datetime as dt
import random

my_email = "obadanindexsam@gmail.com"
password = "xxxxxxxxxxx"

with open("quotes.txt") as file:
    data = file.readlines()

today = dt.datetime.now()

def send_mail(message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="obadansam@gmail.com", 
                    msg=f"Subject: Motivation\n\n{message}")


    print("Mail sent successfully!!")


if today.weekday()==2:
    msg = random.choice(data).strip()
    send_mail(msg)

